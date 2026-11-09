---
symbol: "RWDD3"
type: "gene"
col: 4340
ensembl_id: "ENSG00000122481"
name: "RWD domain containing 3"
location: "1p21.3"
module: 198
arm: "+"
pooled_cpm: 18.84
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 26
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/198"]
generated_by: "tahoemap"
---

# RWDD3

*RWD domain containing 3* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.55× (z +6.6, q 3e-08, up in 22 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.49× (z +6.3, q 1e-07, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.445× (z -17.8, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MORN4]] (+0.76, fdr 7e-06), [[TATDN3]] (+0.73, fdr 7e-06), [[MTFMT]] (+0.70, fdr 7e-06); moves opposite to [[RALY]] (-0.66, fdr 8e-06), [[EGR3]] (-0.62, fdr 1e-05), [[G6PD]] (-0.61, fdr 1e-05).
> It is in [[Module 198]], a single-armed module (Antigen processing: Ubiquitination & Proteasome degradation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CIBAR1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4340.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +6.6 | 3e-08 | 22/43 (Panc 03.27, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.3 | 1e-07 | 33/48 (LoVo, LS 180, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.28×** | +5.4 | 1e-05 | 24/48 (LoVo, RKO, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.36×** | +4.6 | 5e-04 | 21/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.090 | 10/48 (A498, HOP62, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.090 | 10/47 (PANC-1, hTERT-HPNE, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.2 | 0.090 | 17/48 (HCT15, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.090 | 10/47 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.22× | +3.1 | 0.12 | 10/48 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.23× | +3.0 | 0.13 | 11/47 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.13 | 7/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4340.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.445×** | -17.8 | 0e+00 | 38/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.389×** | -14.7 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.386×** | -14.2 | 3e-43 | 42/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.408×** | -13.9 | 8e-42 | 43/47 (SNU-423, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.518×** | -10.2 | 3e-22 | 38/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.292×** | -10.0 | 2e-21 | 38/48 (Hs 766T, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.534×** | -9.7 | 2e-20 | 31/46 (SHP-77, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.542×** | -9.1 | 8e-18 | 35/47 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.561×** | -8.6 | 4e-16 | 31/45 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.564×** | -8.5 | 7e-16 | 30/47 (PANC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.370×** | -8.1 | 4e-14 | 35/45 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.611×** | -7.6 | 1e-12 | 31/47 (MIA PaCa-2, NCI-H23, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.632×** | -7.1 | 5e-11 | 34/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.633×** | -7.1 | 6e-11 | 29/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.731×** | -6.9 | 3e-10 | 27/47 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.004 | 17/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.629×** | -3.8 | 0.004 | 11/48 (C-33 A, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -3.7 | 0.004 | 18/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.852× | -3.5 | 0.011 | 18/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.650×** | -3.5 | 0.011 | 17/46 (AsPC-1, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.876× | -2.9 | 0.082 | 8/48 (HOP62, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4340. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 19.5 | 0 | 11 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -24.8) |
| [[LOX-IMVI (line)]] | wt | 31.7 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.4) |
| [[SW480 (line)]] | alt | 21.3 | 0 | 9 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.242× (z -13.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 28.5 | 0 | 7 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.151× (z -13.0) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.0553× (z -10.4) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 26.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -15.2) |
| [[PANC-1 (line)]] | alt | 14.4 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.211× (z -11.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.353× (z -11.6) |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[A549 (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -11.2) |
| [[J82 (line)]] | alt | 18.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -13.4) |
| [[KATO III (line)]] | alt | 14.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LS 180 (line)]] | wt | 22.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 24.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -12.8) |
| [[SW1417 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 9.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.6) |
| [[C-33 A (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.182× (z -9.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -9.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 23.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -14.3) |
| [[NCI-H2030 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -9.6) |
| [[RKO (line)]] | wt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -11.2) |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0612× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -9.8) ⚠ cell-cycle shift, explains ~70% of this change |
| [[SW 900 (line)]] | alt | 9.87 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -8.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4340), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MORN4]] | +0.76 | +0.70 / +0.78 | both halves | 7e-06 |  |
| [[TATDN3]] | +0.73 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[MTFMT]] | +0.70 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[RNPC3]] | +0.68 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[AGO4]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[SDHAF4]] | +0.67 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[FPGT]] | +0.66 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[FHIP2A]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[THAP3]] | +0.66 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[DSTYK]] | +0.66 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[DCP1B]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DTWD1]] | +0.65 | +0.64 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALY]] | -0.66 | -0.64 / -0.58 | both halves | 8e-06 |  |
| [[EGR3]] | -0.62 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[G6PD]] | -0.61 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[SYS1-DBNDD2]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[ACTN1]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[SYAP1]] | -0.59 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FOS]] | -0.58 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ETF1]] | -0.57 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[EGR1]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MAPKAPK2]] | -0.56 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[SLC25A10]] | -0.56 | -0.53 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CIBAR1]] | C | CIBAR1 activity raises RWDD3's level | lines that do not express CIBAR1 (4) vs lines expressing it (46) | 1.33× lower at baseline in the lines without CIBAR1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-occurs with CTNNB1; also absent: CLTCL1, SPIRE1, ZNF480; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 198]] — Antigen processing: Ubiquitination & Proteasome degradation; 16 genes; every member is in the + arm (projection on the module's main direction 0.846). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.2, 21.1); signed map (-15.4, -13.8). **Vector** length 79.9, 17.3% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +7.1 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +7.0 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.7 | +3.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +0.5 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.5 | -4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.9 | -1.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.8 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | -2.7 | -8.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -2.3 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -2.1 | -0.9 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -2.0 | -0.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -8.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | RWD domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.3 — chr1:95,234,210-95,247,225 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP566K023, RSUME |
| Gene groups (HGNC) | RWD domain containing |
| Reactome | 3 pathways, smallest: SUMO is transferred from E1 to E2 (UBE2I, UBC9); Processing and activation of SUMO; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3V2](https://www.uniprot.org/uniprotkb/Q9Y3V2) (RWD domain-containing protein 3):

> Enhancer of SUMO conjugation. Via its interaction with UBE2I/UBC9, increases SUMO conjugation to proteins by promoting the binding of E1 and E2 enzymes, thioester linkage between SUMO and UBE2I/UBC9 and transfer of SUMO to specific target proteins which include HIF1A, PIAS, NFKBIA, NR3C1 and TOP1. Isoform 1 and isoform 2 positively regulate the NF-kappa-B signaling pathway by enhancing the sumoylation of NF-kappa-B inhibitor alpha (NFKBIA), promoting its stabilization which consequently leads …

**Summary**, from NCBI Gene [25950](https://www.ncbi.nlm.nih.gov/gene/25950):

> Involved in positive regulation of hypoxia-inducible factor-1alpha signaling pathway and positive regulation of protein sumoylation. Predicted to be located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21393) · Entrez [25950](https://www.ncbi.nlm.nih.gov/gene/25950) · UniProt [Q9Y3V2](https://www.uniprot.org/uniprotkb/Q9Y3V2) · Ensembl [ENSG00000122481](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122481)

## Data

Gene col 4340: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4340); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4340, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4340]; `tensor/DDL_lfc|DDL_z.npy` [4340]; `embed/gene_vectors.npy` [4340]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4340 or target_col == 4340). Every well: [[RWDD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RWDD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
