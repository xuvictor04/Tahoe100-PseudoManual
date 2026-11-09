---
symbol: "ANKRA2"
type: "gene"
col: 8932
ensembl_id: "ENSG00000164331"
name: "ankyrin repeat family A member 2"
location: "5q13.2"
module: 62
arm: "+"
pooled_cpm: 25.31
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 25
n_dd_up_clean: 15
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# ANKRA2

*ankyrin repeat family A member 2* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.36× (z +13.8, q 2e-40, up in 41 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +12.5, q 2e-33, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.364× (z -16.8, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.368× (z -8.7, q 1e-15, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPS27L]] (+0.78, fdr 7e-06), [[DDB2]] (+0.77, fdr 7e-06), [[PPM1D]] (+0.76, fdr 7e-06); moves opposite to [[LRP8]] (-0.59, fdr 1e-05), [[PPM1G]] (-0.58, fdr 4e-05), [[BOP1]] (-0.55, fdr 2e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +13.8 | 2e-40 | 41/45 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +12.5 | 2e-33 | 39/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +11.3 | 2e-27 | 36/48 (LOX-IMVI, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +8.2 | 4e-14 | 30/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.6 | 3e-12 | 30/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +6.4 | 1e-08 | 25/48 (A-172, A549, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +6.0 | 2e-07 | 26/48 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.4 | 5e-06 | 26/48 (AsPC-1, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.0 | 4e-05 | 21/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +4.6 | 2e-04 | 16/48 (A-172, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.4 | 5e-04 | 16/38 (A549, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.004 | 18/48 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 13/47 (SNU-423, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 1.17× | +3.8 | 0.006 | 18/48 (A549, A-172, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.008 | 17/48 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.6 | 0.010 | 11/48 (NCI-H2030, RKO, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.010 | 14/46 (HOP62, SW48, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.364×** | -16.8 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.368×** | -8.7 | 1e-15 | 40/47 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.624×** | -7.8 | 9e-13 | 34/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.433×** | -7.3 | 5e-11 | 40/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.434×** | -7.3 | 5e-11 | 37/47 (SW48, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.437×** | -7.2 | 5e-11 | 30/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.437×** | -7.2 | 5e-11 | 31/47 (A498, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.669×** | -6.7 | 2e-09 | 27/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.695×** | -6.0 | 1e-07 | 25/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -5.7 | 5e-07 | 25/46 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.708×** | -5.4 | 3e-06 | 24/48 (MIA PaCa-2, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.651×** | -5.1 | 2e-05 | 27/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.740×** | -5.0 | 3e-05 | 23/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.745×** | -4.9 | 4e-05 | 23/47 (RPMI-7951, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.738×** | -4.7 | 8e-05 | 23/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.695×** | -4.3 | 6e-04 | 15/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.803×** | -3.6 | 0.009 | 14/47 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.3 | 7 (2 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.99× (z +13.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.181× (z -15.1) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 24.9 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.233× (z -12.1) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 31.0 | 6 (1 ⚠) | 1 (1 ⚠) | [[Amsacrine (drug)]] 5 µM 2.96× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.264× (z -9.7) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 26.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.08× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.244× (z -10.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 33.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.42× (z +10.0) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Selinexor (drug)]] 5 µM 2.30× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.210× (z -14.2) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.348× (z -9.6) |
| [[RKO (line)]] | wt | 24.7 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +11.6) | — |
| [[LoVo (line)]] | wt | 50.3 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.276× (z -11.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 32.1 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.64× (z +12.3) ⚠ toxic · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.61× (z +11.3) | — |
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -12.8) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 41.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +11.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -10.3) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 30.4 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.311× (z -11.0) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.395× (z -8.7) |
| [[C32 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -9.5) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 10.1× (z +11.3) ⚠ toxic | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.202× (z -10.4) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.78× (z +9.3) ⚠ toxic | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.55× (z +8.8) ⚠ toxic | — |
| [[RPMI-7951 (line)]] | alt | 21.3 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.223× (z -9.0) |
| [[SW 1271 (line)]] | alt | 45.0 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0820× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS27L]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[DDB2]] | +0.77 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PPM1D]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[DCP1B]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ACTA2]] | +0.71 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[MDM2]] | +0.69 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[FDXR]] | +0.69 | +0.69 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[RRM2B]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[SPATA18]] | +0.68 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ISCU]] | +0.68 | +0.56 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CREBRF]] | +0.67 | +0.67 / +0.58 | both halves | 8e-06 |  |
| [[XPC]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRP8]] | -0.59 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[PPM1G]] | -0.58 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[BOP1]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CS]] | -0.55 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[SMYD3]] | -0.55 | -0.46 / -0.39 | both halves | 5e-05 |  |
| [[RABGAP1L]] | -0.55 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[TMEM201]] | -0.54 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ATAD3A]] | -0.54 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[PGAM5]] | -0.54 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[NAA15]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[PSMG1]] | -0.54 | -0.42 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRA2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens ANKRA2's drug response | lines that do not express PINCR (29) vs lines expressing it (19) | the lines without PINCR respond 0.73× as strongly (z diff +1.17); strongest at Topotecan (hydrochloride) 5 µM: 2.04x vs 3.31x (z diff +2.7) | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[TP53]] | B | TP53 activity strengthens ANKRA2's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.71× as strongly (z diff +1.38); strongest at Topotecan (hydrochloride) 5 µM: 1.98x vs 3.70x (z diff +3.7) | 0.057 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[DDX3Y]] | B | DDX3Y activity raises ANKRA2's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.27× lower at baseline in the lines without DDX3Y | 0.090 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[TRIAP1]] | C | TRIAP1's natural level strengthens ANKRA2's drug response | TRIAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.16; direction clear | 0.039 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |
| [[RPS27L]] | C | RPS27L's natural level strengthens ANKRA2's drug response | RPS27L's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.16; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[MDM2]] | C | MDM2's natural level strengthens ANKRA2's drug response | MDM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.31; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.776). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.8, 35.9); signed map (41.5, -24.6). **Vector** length 125, 35.0% of its response variance represented; |z| ≥ 3 in 1,201 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.56 to 6); *apoptosis* (hallmark, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +8.9 | +13.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +8.8 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | +5.7 | +3.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | +4.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.7 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.6 | -16.8 |
|  | [[EX229 (drug)]] 5 µM |  | -6.5 | -8.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.9 | -7.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.7 | -7.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -7.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.8 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat family A member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:73,552,190-73,565,667 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H9E1](https://www.uniprot.org/uniprotkb/Q9H9E1) (Ankyrin repeat family A protein 2):

> May regulate the interaction between the 3M complex and the histone deacetylases HDAC4 and HDAC5. May also regulate LRP2/megalin (By similarity).

**Summary**, from NCBI Gene [57763](https://www.ncbi.nlm.nih.gov/gene/57763):

> Enables enzyme binding activity and low-density lipoprotein particle receptor binding activity. Involved in regulation of protein-containing complex assembly. Located in 3M complex; cytosol; and plasma membrane. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13208](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13208) · Entrez [57763](https://www.ncbi.nlm.nih.gov/gene/57763) · UniProt [Q9H9E1](https://www.uniprot.org/uniprotkb/Q9H9E1) · Ensembl [ENSG00000164331](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164331)

## Data

Gene col 8932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8932); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8932]; `tensor/DDL_lfc|DDL_z.npy` [8932]; `embed/gene_vectors.npy` [8932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8932 or target_col == 8932). Every well: [[ANKRA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
