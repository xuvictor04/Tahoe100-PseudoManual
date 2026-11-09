---
symbol: "GTF3C3"
type: "gene"
col: 4037
ensembl_id: "ENSG00000119041"
name: "general transcription factor IIIC subunit 3"
location: "2q33.1"
module: 36
arm: "+"
pooled_cpm: 53.61
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 8
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# GTF3C3

*general transcription factor IIIC subunit 3* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.89× (z +17.6, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.563× (z -23.8, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS50]] (+0.72, fdr 7e-06), [[CCT4]] (+0.70, fdr 7e-06), [[GPN1]] (+0.69, fdr 7e-06); moves opposite to [[ERF]] (-0.57, fdr 1e-05), [[POLR2L]] (-0.55, fdr 1e-05), [[NFKBID]] (-0.54, fdr 2e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4037.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.89×** | +17.6 | 0e+00 | 44/48 (A498, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.76×** | +16.6 | 0e+00 | 43/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +15.5 | 0e+00 | 44/48 (A498, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +15.0 | 0e+00 | 43/48 (LoVo, LS 180, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +10.0 | 2e-21 | 31/48 (NCI-H23, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[NG25 (drug)]] 5 µM |  | **1.82×** | +9.1 | 7e-18 | 33/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +8.0 | 1e-13 | 32/43 (SNU-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +7.0 | 2e-10 | 28/49 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +6.4 | 8e-09 | 0/49 | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +6.2 | 2e-08 | 24/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +6.2 | 4e-08 | 25/48 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 5e-08 | 21/48 (HOP62, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +5.7 | 6e-07 | 22/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.36×** | +4.7 | 1e-04 | 17/48 (HCT15, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.35×** | +4.5 | 2e-04 | 14/48 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.051 | 6/48 (PANC-1, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.16× | +3.1 | 0.053 | 4/48 (PANC-1, LOX-IMVI, …) | two highest doses | noisy plate (z scaled) |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 1.11× | +3.1 | 0.060 | 8/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4037.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -23.8 | 0e+00 | 44/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.691×** | -10.4 | 5e-23 | 35/48 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -7.4 | 2e-11 | 23/43 (SW48, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.837× | -7.4 | 2e-11 | 23/48 (A498, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.770×** | -7.4 | 2e-11 | 28/48 (A549, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -6.6 | 5e-09 | 27/49 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.833×** | -5.4 | 7e-06 | 20/48 (A549, J82, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.846× | -4.9 | 6e-05 | 14/48 (RKO, SHP-77, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -4.4 | 6e-04 | 19/48 (SW1417, SW480, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.864× | -4.3 | 9e-04 | 13/48 (LOX-IMVI, H4, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 0.867× | -4.2 | 0.001 | 19/48 (SW 1088, CFPAC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.822×** | -4.1 | 0.002 | 19/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.774×** | -3.9 | 0.004 | 16/48 (RKO, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.874× | -3.3 | 0.037 | 15/45 (SHP-77, NCI-H460, …) | inconsistent across doses | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4037. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 70.6 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.21× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -11.8) |
| [[LoVo (line)]] | wt | 45.9 | 4 | 1 | [[Auranofin (drug)]] 5 µM 2.64× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.2) |
| [[SW480 (line)]] | alt | 68.9 | 2 | 3 | [[Auranofin (drug)]] 5 µM 1.79× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -19.9) |
| [[HOP62 (line)]] | alt | 36.7 | 3 | 1 | [[Auranofin (drug)]] 5 µM 2.60× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -13.3) |
| [[NCI-H460 (line)]] | wt | 80.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -15.5) |
| [[C32 (line)]] | wt | 50.6 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -8.7) |
| [[LS 180 (line)]] | wt | 48.8 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -12.7) |
| [[RKO (line)]] | wt | 78.3 | 2 | 1 | [[Auranofin (drug)]] 5 µM 2.41× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -19.1) |
| [[SW48 (line)]] | wt | 68.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.0) |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -11.1) |
| [[J82 (line)]] | alt | 60.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 51.9 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.18× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -18.2) |
| [[NCI-H1573 (line)]] | alt | 62.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 70.2 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.395× (z -11.7) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 79.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -10.9) |
| [[PANC-1 (line)]] | alt | 65.3 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 1.78× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -11.8) |
| [[SHP-77 (line)]] | alt | 63.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -14.2) |
| [[A549 (line)]] | wt | 47.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 39.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -8.7) |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.0) |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 52.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0873× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 34.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.2) |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.9) |
| [[KATO III (line)]] | alt | 38.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 42.6 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.12× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 46.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 61.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -11.9) |
| [[SW 900 (line)]] | alt | 42.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -13.3) |
| [[SW1417 (line)]] | alt | 52.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -12.6) |
| [[A-172 (line)]] | wt | 38.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 57.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4037), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS50]] | +0.72 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[CCT4]] | +0.70 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[GPN1]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[CWC27]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[NUDC]] | +0.68 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[GFM2]] | +0.66 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[PSMC1]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NRDE2]] | +0.65 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[ERCC3]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[APOOL]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[OPA1]] | +0.65 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[PSMD12]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERF]] | -0.57 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[POLR2L]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 | pathway: RNA Polymerase III Abortive And Retractive Initiation; STRING 512 |
| [[NFKBID]] | -0.54 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TNRC6C]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GTF3C3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ANKEF1]] | B | ANKEF1 activity lowers GTF3C3's level | lines that do not express ANKEF1 (6) vs lines expressing it (44) | 1.36× higher at baseline in the lines without ANKEF1 | 0.063 | ⚠ within organs, on part of the lines; also absent: EPAS1, TMEM51, PC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-23.2, -8.1); signed map (-21.8, -21.9). **Vector** length 110, 27.0% of its response variance represented; |z| ≥ 3 in 1,048 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.9 | +16.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +9.5 | +10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +17.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.2 | +15.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.7 | +15.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.9 | +6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +4.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -23.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -4.4 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | -7.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.9 | -3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | general transcription factor IIIC subunit 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:196,763,035-196,799,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TFiiiC2-102, TFIIIC102 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; General transcription factor IIIC complex subunits |
| Reactome | 5 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5Q9](https://www.uniprot.org/uniprotkb/Q9Y5Q9) (General transcription factor 3C polypeptide 3):

> Involved in RNA polymerase III-mediated transcription. Integral, tightly associated component of the DNA-binding TFIIIC2 subcomplex that directly binds tRNA and virus-associated RNA promoters.

**Summary**, from NCBI Gene [9330](https://www.ncbi.nlm.nih.gov/gene/9330):

> The protein encoded by this gene is part of the TFIIIC2 complex, which binds to the promoters of small nuclear and cytoplasmic RNA genes in order to recruit RNA polymerase III. The TFIIIC2 complex is composed of six subunits. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:4666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4666) · Entrez [9330](https://www.ncbi.nlm.nih.gov/gene/9330) · UniProt [Q9Y5Q9](https://www.uniprot.org/uniprotkb/Q9Y5Q9) · Ensembl [ENSG00000119041](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119041)

## Data

Gene col 4037: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4037); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4037, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4037]; `tensor/DDL_lfc|DDL_z.npy` [4037]; `embed/gene_vectors.npy` [4037]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4037 or target_col == 4037). Every well: [[GTF3C3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
