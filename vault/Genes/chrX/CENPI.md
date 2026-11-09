---
symbol: "CENPI"
type: "gene"
col: 2243
ensembl_id: "ENSG00000102384"
name: "centromere protein I"
location: "Xq22.1"
module: 67
arm: "+"
pooled_cpm: 42.19
n_lines_expressing: 48
n_dd_up: 9
n_dd_down: 32
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CENPI

*centromere protein I* — Xq22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.20× (z +11.6, q 3e-28, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 5 µM: 1.71× (z +4.1, q 0.004, up in 17 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 6 lines (NCI-H23 3.21×, SW480 3.16×, A549 3.56×, NCI-H460 3.41×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 2.86×, NCI-H460 3.37×, A549 3.34×, NCI-H23 2.54×; ⚠ cell-cycle shift, explains ~32% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H23 2.75×, SW480 2.62×; ⚠ cell-cycle shift, explains ~36% of this change).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.444× (z -16.9, q 0e+00, down in 37 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIT]] (+0.91, fdr 7e-06), [[PBK]] (+0.87, fdr 7e-06), [[NEIL3]] (+0.86, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 1 goes from it, the strongest it → [[POC1A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2243.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Panobinostat (drug)]] 5 µM in 6 lines (NCI-H23 3.21×, SW480 3.16×, A549 3.56×, NCI-H460 3.41×, …; ⚠ cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 0.5 µM in 4 lines (SW480 2.86×, NCI-H460 3.37×, A549 3.34×, NCI-H23 2.54×; ⚠ cell-cycle shift, explains ~32% of this change); [[Belinostat (drug)]] 5 µM in 2 lines (NCI-H23 2.75×, SW480 2.62×; ⚠ cell-cycle shift, explains ~36% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.20×** | +11.6 | 3e-28 | 39/46 (NCI-H23, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.02×** | +10.3 | 1e-22 | 36/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.99×** | +10.1 | 9e-22 | 37/46 (NCI-H23, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.35×** | +4.3 | 0.003 | 14/38 (Panc 03.27, NCI-H2347, …) | top dose only | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.71×** | +4.1 | 0.004 | 17/45 (NCI-H2030, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.30×** | +3.8 | 0.012 | 19/46 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.012 | 17/46 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.28×** | +3.7 | 0.017 | 15/46 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.4 | 0.040 | 1/46 (SW 1271) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.16× | +3.2 | 0.083 | 11/46 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.24×** | +3.1 | 0.086 | 11/45 (A549, PANC-1, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.23× | +3.1 | 0.10 | 14/46 (LoVo, HOP62, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | 1.34× | +3.0 | 0.10 | 8/46 (Hs 766T, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2243.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.444×** | -16.9 | 0e+00 | 37/45 (Hs 766T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.377×** | -14.3 | 4e-44 | 39/45 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.502×** | -14.3 | 4e-44 | 40/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.510×** | -14.0 | 2e-42 | 42/46 (CFPAC-1, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.425×** | -12.1 | 1e-31 | 38/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.500×** | -10.2 | 2e-22 | 39/46 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.520×** | -9.6 | 6e-20 | 33/46 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -8.4 | 2e-15 | 31/46 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.606×** | -6.6 | 3e-09 | 33/46 (H4, HOP62, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.442×** | -6.3 | 2e-08 | 28/40 (SHP-77, C32, …) | all doses, flat | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -5.6 | 1e-06 | 27/46 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -5.2 | 1e-05 | 25/46 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.524×** | -5.0 | 3e-05 | 21/46 (SW480, HOP62, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.721×** | -4.8 | 7e-05 | 27/46 (HT-29, SNU-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.723×** | -4.8 | 7e-05 | 23/45 (LS 180, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[palbociclib (drug)]] 5 µM |  | **0.547×** | -4.6 | 1e-04 | 20/45 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **0.806×** | -4.5 | 2e-04 | 20/46 (C32, SW1417, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.820×** | -4.1 | 1e-03 | 20/46 (A549, LOX-IMVI, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.595×** | -4.0 | 0.002 | 22/46 (LS 180, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2243. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 57.9 | 2 (2 ⚠) | 17 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.41× (z +9.3) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -16.8) |
| [[A549 (line)]] | wt | 40.5 | 2 (2 ⚠) | 13 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.56× (z +9.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.1) |
| [[SW480 (line)]] | alt | 58.5 | 3 (3 ⚠) | 8 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.16× (z +11.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.0) |
| [[A498 (line)]] | wt | 34.6 | 1 (1 ⚠) | 9 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.54× (z +8.5) ⚠ cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 38.3 | 1 (1 ⚠) | 7 | [[Panobinostat (drug)]] 5 µM 4.24× (z +9.1) ⚠ cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.238× (z -12.7) |
| [[H4 (line)]] | wt | 39.5 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 52.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0913× (z -18.1) |
| [[HEC-1-A (line)]] | alt | 58.3 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.5) |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 6 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.156× (z -14.6) |
| [[A-427 (line)]] | wt | 97.7 | 0 | 5 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.304× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 53.2 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -13.5) |
| [[HOP62 (line)]] | alt | 51.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -15.3) |
| [[Hs 766T (line)]] | wt | 44.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 79.1 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 3.21× (z +11.2) ⚠ cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -10.5) |
| [[J82 (line)]] | alt | 97.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.4) |
| [[PANC-1 (line)]] | alt | 90.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.335× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 25.3 | 0 | 3 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.196× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.137× (z -17.2) |
| [[KATO III (line)]] | alt | 39.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.166× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 14.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 46.6 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.322× (z -9.0) |
| [[SNU-1 (line)]] | wt | 42.3 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.284× (z -9.4) |
| [[SW48 (line)]] | wt | 25.1 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.141× (z -8.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.6) |
| [[A-172 (line)]] | wt | 24.8 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.329× (z -9.2) |
| [[BT-474 (line)]] | alt | 20.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -9.3) |
| [[HCT15 (line)]] | alt | 45.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -10.1) |
| [[HT-29 (line)]] | alt | 31.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.386× (z -8.5) |
| [[LoVo (line)]] | wt | 15.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.223× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.372× (z -10.3) |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 56.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -15.2) |
| [[SW1417 (line)]] | alt | 42.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.383× (z -9.7) |
| [[AN3 CA (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 59.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2243), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIT]] | +0.91 | +0.90 / +0.88 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[PBK]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 | STRING 586 |
| [[NEIL3]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | STRING 486 |
| [[SPC24]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 781 |
| [[MELK]] | +0.86 | +0.86 / +0.89 | both halves | 7e-06 | STRING 691 |
| [[NCAPG2]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 | STRING 502 |
| [[PARPBP]] | +0.86 | +0.84 / +0.83 | both halves | 7e-06 | STRING 710 |
| [[IQGAP3]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | pathway: RHO GTPase Effectors |
| [[UBE2T]] | +0.85 | +0.85 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SKA1]] | +0.84 | +0.83 / +0.82 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 805 |
| [[CEP55]] | +0.84 | +0.81 / +0.85 | both halves | 7e-06 | STRING 647 |
| [[AURKB]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 804 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CENPI's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NDC80]] | C | NDC80 activity raises CENPI's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.70× lower at baseline in the lines without NDC80 | 0.056 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CENPI's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.18× lower at baseline in the lines without AURKB | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[SAPCD2]], [[SHMT1]] | C | SAPCD2, SHMT1 activity raises CENPI's level | lines that do not express SAPCD2, SHMT1 (3) vs lines expressing them (47) | 2.39× lower at baseline in the lines without SAPCD2, SHMT1 | 0.068 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent genes |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POC1A]] | C | CENPI's natural level strengthens POC1A's drug response | CENPI's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.03; direction clear | 0.092 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.895). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.4, -53.0); signed map (-45.8, -41.1). **Vector** length 146, 49.6% of its response variance represented; |z| ≥ 3 in 1,311 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.78 to 12); *G2/M checkpoint* (hallmark, mean cos +0.77 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +7.9 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.4 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.4 | +10.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.6 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.3 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.1 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -10.7 | -14.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.0 | -14.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -8.6 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -14.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.2 | -9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.0 | -3.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.4 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein I |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.1 — chrX:101,098,188-101,166,126 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRPR1, CENP-I, Mis6; previously FSHPRH1 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92674](https://www.uniprot.org/uniprotkb/Q92674) (Centromere protein I):

> Component of the CENPA-CAD (nucleosome distal) complex, a complex recruited to centromeres which is involved in assembly of kinetochore proteins, mitotic progression and chromosome segregation. May be involved in incorporation of newly synthesized CENPA into centromeres via its interaction with the CENPA-NAC complex. Required for the localization of CENPF, MAD1L1 and MAD2 (MAD2L1 or MAD2L2) to kinetochores. Involved in the response of gonadal tissues to follicle-stimulating hormone.

**Summary**, from NCBI Gene [2491](https://www.ncbi.nlm.nih.gov/gene/2491):

> This gene encodes a centromere protein that is a component of the CENPA-NAC (nucleosome-associated) complex. This complex is critical for accurate chromosome alignment and segregation and it ensures proper mitotic progression. This protein regulates the recruitment of kinetochore-associated proteins that are required to generate the spindle checkpoint signal. The product of this gene is involved in the response of gonadal tissues to follicle-stimulating hormone. Mutations in this gene may be …

**Accessions** — [HGNC:3968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3968) · Entrez [2491](https://www.ncbi.nlm.nih.gov/gene/2491) · UniProt [Q92674](https://www.uniprot.org/uniprotkb/Q92674) · Ensembl [ENSG00000102384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102384)

## Data

Gene col 2243: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2243); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2243, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2243]; `tensor/DDL_lfc|DDL_z.npy` [2243]; `embed/gene_vectors.npy` [2243]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2243 or target_col == 2243). Every well: [[CENPI — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPI.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
