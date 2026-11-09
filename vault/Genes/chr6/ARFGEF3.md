---
symbol: "ARFGEF3"
type: "gene"
col: 3366
ensembl_id: "ENSG00000112379"
name: "ARFGEF family member 3"
location: "6q23.3-q24.1"
module: 180
arm: "+"
pooled_cpm: 181.23
n_lines_expressing: 44
n_dd_up: 3
n_dd_down: 38
n_dd_up_clean: 2
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# ARFGEF3

*ARFGEF family member 3* — 6q23.3-q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.37× (z +6.2, q 3e-07, up in 29 of 42 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 5 µM: 1.49× (z +4.1, q 0.014, up in 29 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (PANC-1 2.01×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2030 2.36×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.213× (z -42.8, q 0e+00, down in 42 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYBG3]] (+0.71, fdr 7e-06), [[NGLY1]] (+0.71, fdr 7e-06), [[YEATS2]] (+0.70, fdr 7e-06); moves opposite to [[HNRNPH3]] (-0.52, fdr 5e-05), [[MDFIC]] (-0.52, fdr 1e-04), [[RPRD1B]] (-0.51, fdr 2e-04).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[GALNT18]] → it (grade B ⚠); 3 go from it, the strongest it → [[GALNT18]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3366.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 1 line (PANC-1 2.01×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2030 2.36×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.37×** | +6.2 | 3e-07 | 29/42 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.014 | 29/42 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.015 | 25/42 (SNU-423, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | 1.38× | +3.3 | 0.12 | 19/42 (NCI-H2030, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 1.26× | +3.3 | 0.12 | 19/42 (HOP62, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.12× | +3.2 | 0.15 | 5/42 (J82, PANC-1, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.18 | 16/42 (J82, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.213×** | -42.8 | 0e+00 | 42/42 (HEC-1-A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.264×** | -25.0 | 0e+00 | 42/42 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.358×** | -20.1 | 0e+00 | 40/42 (HEC-1-A, C32, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -18.7 | 0e+00 | 40/43 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.381×** | -18.1 | 0e+00 | 40/41 (MIA PaCa-2, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.450×** | -15.0 | 0e+00 | 39/41 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.451×** | -14.4 | 6e-45 | 39/39 (RKO, SW48, …) | all doses, flat | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.470×** | -14.2 | 8e-44 | 33/38 (NCI-H23, C32, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.505×** | -13.3 | 1e-38 | 38/43 (C32, NCI-H23, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.560×** | -11.3 | 6e-28 | 37/42 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.668×** | -11.1 | 4e-27 | 32/42 (C32, SK-MEL-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.584×** | -10.5 | 5e-24 | 36/42 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.597×** | -10.1 | 4e-22 | 33/42 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.631×** | -9.0 | 1e-17 | 34/42 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.635×** | -8.8 | 4e-17 | 34/42 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.729×** | -8.7 | 1e-16 | 35/42 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.632×** | -8.6 | 3e-16 | 34/42 (SK-MEL-2, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -8.1 | 1e-14 | 32/43 (MIA PaCa-2, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.677×** | -7.6 | 1e-12 | 36/42 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.534×** | -6.4 | 4e-09 | 29/42 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -5.2 | 5e-06 | 25/42 (C32, BT-474, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.794×** | -4.5 | 2e-04 | 25/42 (SW 1088, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.806×** | -4.2 | 6e-04 | 24/42 (C32, HOP62, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.802×** | -4.1 | 8e-04 | 21/42 (PANC-1, C32, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.801×** | -4.1 | 9e-04 | 22/42 (HOP62, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 444 | 0 | 22 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0510× (z -47.9) |
| [[MIA PaCa-2 (line)]] | alt | 184 | 0 | 21 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -41.5) |
| [[HEC-1-A (line)]] | alt | 254 | 0 | 20 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0523× (z -52.8) |
| [[LOX-IMVI (line)]] | wt | 211 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0881× (z -36.8) |
| [[HOP62 (line)]] | alt | 207 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -34.6) |
| [[A549 (line)]] | wt | 160 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0952× (z -41.7) |
| [[SNU-423 (line)]] | alt | 434 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -35.7) |
| [[HepG2_C3A (line)]] | wt | 458 | 0 | 13 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0850× (z -26.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.242× (z -22.8) |
| [[NCI-H1792 (line)]] | alt | 270 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -51.6) |
| [[NCI-H460 (line)]] | wt | 122 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -29.2) |
| [[A-172 (line)]] | wt | 272 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -33.5) |
| [[J82 (line)]] | alt | 198 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -37.3) |
| [[SK-MEL-2 (line)]] | alt | 147 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -30.0) |
| [[HS-578T (line)]] | alt | 111 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -22.9) |
| [[LoVo (line)]] | wt | 287 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -27.0) |
| [[PANC-1 (line)]] | alt | 68.9 | 1 | 9 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.01× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -24.2) |
| [[RKO (line)]] | wt | 331 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -25.1) |
| [[BT-474 (line)]] | alt | 175 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -20.0) |
| [[C-33 A (line)]] | alt | 370 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -15.4) |
| [[KATO III (line)]] | alt | 286 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -17.9) |
| [[SW480 (line)]] | alt | 160 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -21.4) |
| [[LS 180 (line)]] | wt | 282 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -19.2) |
| [[RPMI-7951 (line)]] | alt | 91.9 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -25.8) |
| [[HCT15 (line)]] | alt | 339 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -21.5) |
| [[Hs 766T (line)]] | wt | 148 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -23.5) |
| [[NCI-H1573 (line)]] | alt | 132 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -21.3) |
| [[SW 900 (line)]] | alt | 199 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -23.9) |
| [[SW48 (line)]] | wt | 319 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -23.0) |
| [[NCI-H2030 (line)]] | alt | 124 | 1 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.36× (z +9.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 129 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0998× (z -25.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -30.0) |
| [[SW1417 (line)]] | alt | 107 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -23.6) |
| [[H4 (line)]] | wt | 131 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0636× (z -32.2) |
| [[HT-29 (line)]] | alt | 278 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -20.4) |
| [[SHP-77 (line)]] | alt | 294 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.385× (z -10.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.516× (z -10.4) |
| [[COLO 205 (line)]] | alt | 143 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.562× (z -8.7) |
| [[NCI-H2347 (line)]] | alt | 92.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -23.9) |
| [[SW 1271 (line)]] | alt | 227 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -23.7) |
| [[A-427 (line)]] | wt | 207 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.535× (z -8.6) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 57.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.6) |
| [[A498 (line)]] | wt | 28.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 43.0 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 22.2 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 28.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 66.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBG3]] | +0.71 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[NGLY1]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.70 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.67 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[SMAP1]] | +0.64 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[RIMKLA]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D9B]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PPFIA1]] | +0.61 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TPD52]] | +0.60 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.60 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NUP58]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH3]] | -0.52 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[MDFIC]] | -0.52 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[RPRD1B]] | -0.51 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[GTF3C6]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[LUC7L2]] | -0.50 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[PMF1]] | -0.49 | -0.39 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT18]] | B | GALNT18 activity raises ARFGEF3's level | lines that do not express GALNT18 (10) vs lines expressing it (40) | 1.61× lower at baseline in the lines without GALNT18 | 0.056 | ⚠ within organs, on part of the lines; also absent: SERTAD4, ULK2, WNT9A |
| [[TOP2A]] | B | TOP2A activity raises ARFGEF3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RIMKLA]] | B | RIMKLA activity raises ARFGEF3's level | lines that do not express RIMKLA (8) vs lines expressing it (42) | 2.70× lower at baseline in the lines without RIMKLA | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000290927, PLEKHH1, NRTN; its own permutation p |
| [[ARHGEF10]] | B | ARHGEF10 activity lowers ARFGEF3's level | lines that do not express ARHGEF10 (8) vs lines expressing it (42) | 2.34× higher at baseline in the lines without ARHGEF10 | 0.093 | ⚠ within organs, on part of the lines; also absent: LY6E |
| [[PFKP]] | C | PFKP activity raises ARFGEF3's level | lines that do not express PFKP (3) vs lines expressing it (47) | 3.27× lower at baseline in the lines without PFKP | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ASPH, MAP3K5, CFAP45; maybe low, not absent; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT18]] | B | ARFGEF3 activity raises GALNT18's level | lines that do not express ARFGEF3 (6) vs lines expressing it (44) | 2.43× lower at baseline in the lines without ARFGEF3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ARHGEF37, RHBDF2, DBNDD1; maybe low, not absent |
| [[LINC00887]] | B | ARFGEF3 activity raises LINC00887's level | lines that do not express ARFGEF3 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without ARFGEF3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ARHGEF37, RHBDF2, DBNDD1; maybe low, not absent |
| [[PFKP]] | B | ARFGEF3 activity raises PFKP's level | lines that do not express ARFGEF3 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without ARFGEF3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ARHGEF37, RHBDF2, DBNDD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.9, -16.0); signed map (-36.9, 26.3). **Vector** length 119, 46.3% of its response variance represented; |z| ≥ 3 in 1,450 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.9 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +6.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.9 | +2.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.8 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | +5.5 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.8 | +3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.7 | +2.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.9 | -11.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.5 | -8.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -15.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -4.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | ARFGEF family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.3-q24.1 — chr6:138,161,939-138,344,663 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ171N11.1, BIG3, PPP1R33; previously C6orf92, KIAA1244 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Armadillo like helical domain containing; ArfGEF family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TH69](https://www.uniprot.org/uniprotkb/Q5TH69) (Brefeldin A-inhibited guanine nucleotide-exchange protein 3):

> Participates in the regulation of systemic glucose homeostasis, where it negatively regulates insulin granule biogenesis in pancreatic islet beta cells (By similarity). Also regulates glucagon granule production in pancreatic alpha cells (By similarity). Inhibits nuclear translocation of the transcriptional coregulator PHB2 and may enhance estrogen receptor alpha (ESR1) transcriptional activity in breast cancer cells.

**Summary**, from NCBI Gene [57221](https://www.ncbi.nlm.nih.gov/gene/57221):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in vesicle-mediated transport. Predicted to be located in transport vesicle membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21213](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21213) · Entrez [57221](https://www.ncbi.nlm.nih.gov/gene/57221) · UniProt [Q5TH69](https://www.uniprot.org/uniprotkb/Q5TH69) · Ensembl [ENSG00000112379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112379)

## Data

Gene col 3366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3366); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3366]; `tensor/DDL_lfc|DDL_z.npy` [3366]; `embed/gene_vectors.npy` [3366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3366 or target_col == 3366). Every well: [[ARFGEF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARFGEF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
