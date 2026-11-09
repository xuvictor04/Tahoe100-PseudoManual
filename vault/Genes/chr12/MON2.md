---
symbol: "MON2"
type: "gene"
col: 706
ensembl_id: "ENSG00000061987"
name: "MON2 regulator of endosome-to-Golgi trafficking"
location: "12q14.1"
module: 56
arm: "+"
pooled_cpm: 296.53
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# MON2

*MON2 regulator of endosome-to-Golgi trafficking* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.65× (z +4.8, q 8e-04, up in 32 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (A498 4.52×, LOX-IMVI 3.47×, A-427 3.41×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 2.10×, BT-474 1.90×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (BT-474 2.03×, SNU-1 2.18×).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.358× (z -18.2, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.746× (z -5.4, q 4e-06, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRP54]] (+0.74, fdr 7e-06), [[MCEE]] (+0.74, fdr 7e-06), [[SEC31A]] (+0.71, fdr 7e-06).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TBC1D23]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 706.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 3 lines (A498 4.52×, LOX-IMVI 3.47×, A-427 3.41×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-427 2.10×, BT-474 1.90×; ⚠ cell-cycle shift, would explain all of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (BT-474 2.03×, SNU-1 2.18×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +4.8 | 8e-04 | 32/49 (A498, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.053 | 26/48 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.25 | 18/48 (A498, A-427, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 19 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.358×** | -18.2 | 0e+00 | 43/44 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.399×** | -16.9 | 0e+00 | 49/49 (NCI-H1792, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **0.684×** | -7.0 | 6e-10 | 44/48 (Hs 766T, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.693×** | -6.7 | 2e-09 | 39/48 (HOP62, A549, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -6.6 | 5e-09 | 35/47 (KATO III, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.697×** | -6.1 | 9e-08 | 28/45 (CFPAC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.720×** | -6.0 | 1e-07 | 35/48 (A498, HOP62, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.793×** | -5.6 | 2e-06 | 30/49 (A549, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.746×** | -5.4 | 4e-06 | 29/48 (AsPC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.746×** | -5.4 | 4e-06 | 34/48 (HOP62, A498, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.746×** | -5.2 | 1e-05 | 30/47 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.843× | -4.2 | 0.001 | 21/48 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.798×** | -4.1 | 0.002 | 31/48 (A549, SW 900, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.806×** | -3.8 | 0.006 | 26/48 (H4, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.818×** | -3.7 | 0.009 | 26/48 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -3.7 | 0.009 | 24/48 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.010 | 26/48 (CFPAC-1, H4, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.847× | -3.0 | 0.068 | 19/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.076 | 17/48 (LS 180, A549, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.852× | -2.9 | 0.083 | 17/48 (COLO 205, KATO III, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.886× | -2.9 | 0.097 | 15/48 (HOP62, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 382 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -18.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 246 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.559× (z -8.5) |
| [[Hs 766T (line)]] | wt | 260 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -15.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 353 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.204× (z -17.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 260 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 200 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.399× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.505× (z -8.6) |
| [[A549 (line)]] | wt | 371 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -13.4) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 277 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -14.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 292 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 363 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 295 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.41× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 342 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -13.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 221 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +9.9) | — |
| [[C32 (line)]] | wt | 247 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -13.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 302 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.246× (z -19.4) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 242 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -14.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 294 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.47× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.349× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 391 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -20.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 282 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -17.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 328 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -15.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 238 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -14.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 415 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -18.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 408 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -16.3) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 341 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -17.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 211 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.380× (z -10.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 255 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -10.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 444 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.225× (z -15.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 394 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -19.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 359 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 358 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -14.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 258 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 367 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -10.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 264 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -16.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -14.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 325 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -13.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 327 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -16.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 316 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 226 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -9.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 186 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.466× (z -10.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 350 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -18.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 223 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -22.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 369 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -11.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 309 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -15.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 251 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 291 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 309 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 260 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 208 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP54]] | +0.74 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[MCEE]] | +0.74 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.71 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[ACBD3]] | +0.70 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.70 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[GPR107]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[COG6]] | +0.69 | +0.74 / +0.75 | both halves | 7e-06 | STRING 424 |
| [[SEC61B]] | +0.67 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SLC39A9]] | +0.66 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[UFM1]] | +0.66 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[COPA]] | +0.65 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[RAB1A]] | +0.65 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBC1D23]] | C | TBC1D23's natural level strengthens MON2's drug response | TBC1D23's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.34; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[COPB2]] | C | COPB2's natural level strengthens MON2's drug response | COPB2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.11; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.712). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, -34.7); signed map (-51.4, 11.8). **Vector** length 116, 47.6% of its response variance represented; |z| ≥ 3 in 1,125 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.57 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.61 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.61 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +2.8 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | -16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | -1.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.2 | +0.8 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.1 | +1.0 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | +2.0 | +0.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +1.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.0 | +0.6 |
| fall | [[TAK-901 (drug)]] 0.05 µM |  | -4.6 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.0 | -4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MON2 regulator of endosome-to-Golgi trafficking |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:62,466,817-62,600,476 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1040 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z3U7](https://www.uniprot.org/uniprotkb/Q7Z3U7) (Protein MON2 homolog):

> Plays a role in regulating membrane trafficking of cargo proteins. Together with ATP9A and DOP1B, regulates SNX3 retromer-mediated endosomal sorting of WLS away from lysosomal degradation.

**Summary**, from NCBI Gene [23041](https://www.ncbi.nlm.nih.gov/gene/23041):

> Predicted to enable guanyl-nucleotide exchange factor activity. Predicted to be involved in Golgi to endosome transport; protein targeting to vacuole; and retrograde transport, endosome to Golgi. Located in Golgi apparatus and early endosome membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29177) · Entrez [23041](https://www.ncbi.nlm.nih.gov/gene/23041) · UniProt [Q7Z3U7](https://www.uniprot.org/uniprotkb/Q7Z3U7) · Ensembl [ENSG00000061987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061987)

## Data

Gene col 706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 706); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 706]; `tensor/DDL_lfc|DDL_z.npy` [706]; `embed/gene_vectors.npy` [706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 706 or target_col == 706). Every well: [[MON2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MON2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
