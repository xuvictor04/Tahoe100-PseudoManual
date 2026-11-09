---
symbol: "GFPT1"
type: "gene"
col: 12581
ensembl_id: "ENSG00000198380"
name: "glutamine--fructose-6-phosphate transaminase 1"
location: "2p13.3"
module: 56
arm: "+"
pooled_cpm: 386.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 42
n_dd_up_clean: 5
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# GFPT1

*glutamine--fructose-6-phosphate transaminase 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.36× (z +7.1, q 7e-10, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~23% of this change. The strongest without an alert is [[Artesunate (drug)]] 0.5 µM: 1.29× (z +4.9, q 3e-04, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.329× (z -24.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERPUD1]] (+0.82, fdr 7e-06), [[SEC63]] (+0.80, fdr 7e-06), [[SEC23A]] (+0.79, fdr 7e-06); moves opposite to [[PNRC2]] (-0.62, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[GALNT3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +7.1 | 7e-10 | 36/48 (SW480, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **1.29×** | +4.9 | 3e-04 | 32/48 (SW480, H4, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 6e-04 | 33/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.3 | 0.002 | 27/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.002 | 28/47 (SW480, HCT15, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.006 | 22/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.011 | 23/49 (MIA PaCa-2, SW1417, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.3 | 0.075 | 21/48 (SW480, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.0 | 0.14 | 13/49 (COLO 205, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 51 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.329×** | -24.3 | 0e+00 | 46/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.326×** | -20.3 | 0e+00 | 44/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.438×** | -18.7 | 0e+00 | 46/49 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.451×** | -15.0 | 0e+00 | 45/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.469×** | -14.3 | 4e-44 | 45/48 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.620×** | -11.7 | 1e-29 | 45/48 (NCI-H2347, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.492×** | -11.2 | 2e-27 | 46/48 (NCI-H2347, H4, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -11.0 | 2e-26 | 42/47 (NCI-H2347, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.580×** | -9.9 | 4e-21 | 41/48 (H4, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.612×** | -9.2 | 1e-18 | 39/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.618×** | -9.1 | 6e-18 | 42/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.637×** | -8.5 | 1e-15 | 36/48 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.654×** | -7.7 | 6e-13 | 35/50 (H4, HS-578T, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.645×** | -7.6 | 8e-13 | 45/47 (LoVo, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.670×** | -7.5 | 2e-12 | 36/48 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.661×** | -7.5 | 2e-12 | 38/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -6.4 | 4e-09 | 36/48 (NCI-H2347, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -5.6 | 5e-07 | 31/49 (CFPAC-1, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **0.817×** | -3.8 | 0.003 | 24/49 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.788×** | -3.8 | 0.004 | 28/49 (LS 180, RKO, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.695×** | -3.6 | 0.007 | 22/47 (AsPC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 693 | 0 | 23 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -26.3) |
| [[NCI-H2347 (line)]] | alt | 542 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -31.5) |
| [[LoVo (line)]] | wt | 737 | 0 | 18 (11 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0981× (z -24.7) |
| [[CFPAC-1 (line)]] | alt | 457 | 0 | 17 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -26.0) |
| [[A-172 (line)]] | wt | 431 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -23.2) |
| [[HT-29 (line)]] | alt | 866 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -25.0) |
| [[KATO III (line)]] | alt | 912 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.4) |
| [[AsPC-1 (line)]] | alt | 469 | 1 (1 ⚠) | 12 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.39× (z +11.8) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -37.4) |
| [[HS-578T (line)]] | alt | 409 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -23.8) |
| [[A498 (line)]] | wt | 746 | 1 | 11 (4 ⚠) | [[Auranofin (drug)]] 5 µM 1.57× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.270× (z -25.2) |
| [[HOP62 (line)]] | alt | 399 | 0 | 11 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.329× (z -20.2) |
| [[Hs 766T (line)]] | wt | 280 | 0 | 11 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -17.9) |
| [[SW 900 (line)]] | alt | 521 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.3) |
| [[COLO 205 (line)]] | alt | 665 | 1 (1 ⚠) | 9 (5 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.78× (z +13.7) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 421 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.8) |
| [[NCI-H1573 (line)]] | alt | 242 | 0 | 9 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -19.4) |
| [[NCI-H1792 (line)]] | alt | 416 | 0 | 9 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -17.9) |
| [[A-427 (line)]] | wt | 316 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -13.9) |
| [[SW1417 (line)]] | alt | 420 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -16.6) |
| [[PANC-1 (line)]] | alt | 246 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -14.8) |
| [[SW480 (line)]] | alt | 260 | 4 (2 ⚠) | 3 (1 ⚠) | [[Artesunate (drug)]] 5 µM 2.10× (z +12.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Artesunate (drug)]] 0.5 µM 1.87× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.420× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 370 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -19.2) |
| [[Panc 03.27 (line)]] | alt | 261 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 470 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -20.5) |
| [[SNU-423 (line)]] | alt | 208 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -15.0) |
| [[SW48 (line)]] | wt | 356 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.269× (z -11.0) |
| [[A549 (line)]] | wt | 340 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -14.8) |
| [[J82 (line)]] | alt | 177 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -17.6) |
| [[SW 1088 (line)]] | alt | 566 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.1) |
| [[BT-474 (line)]] | alt | 153 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -13.2) |
| [[HCT15 (line)]] | alt | 527 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.198× (z -13.4) |
| [[LS 180 (line)]] | wt | 562 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 329 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -10.9) |
| [[RKO (line)]] | wt | 230 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 310 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.2) |
| [[MIA PaCa-2 (line)]] | alt | 191 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 307 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.218× (z -11.9) |
| [[SNU-1 (line)]] | wt | 353 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -15.0) |
| [[C32 (line)]] | wt | 171 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 281 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 162 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.437× (z -9.1) |
| [[SHP-77 (line)]] | alt | 164 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -12.0) |
| [[AN3 CA (line)]] | alt | 177 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 353 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 284 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERPUD1]] | +0.82 | +0.82 / +0.76 | both halves | 7e-06 | pathway: Unfolded Protein Response (UPR) |
| [[SEC63]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[SEC23A]] | +0.79 | +0.83 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COPB1]] | +0.79 | +0.80 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SEC24D]] | +0.79 | +0.81 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[SLC31A1]] | +0.79 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[GARS1]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[COG6]] | +0.77 | +0.82 / +0.66 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDXDC2P]] | +0.77 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[HSPA5]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[PRRC1]] | +0.76 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC2]] | -0.62 | -0.63 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises GFPT1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.48× lower at baseline in the lines without GALNT3 | 0.048 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[MCTP2]] | B | MCTP2 activity raises GFPT1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without MCTP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[MCTP2]] | B | MCTP2 activity strengthens GFPT1's drug response | lines that do not express MCTP2 (20) vs lines expressing it (29) | the lines without MCTP2 respond 0.76× as strongly (z diff +1.80); strongest at Digitoxin 5 µM: 0.74x vs 0.49x (z diff +3.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises GFPT1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ADM2]] | B | ADM2 activity raises GFPT1's level | lines that do not express ADM2 (9) vs lines expressing it (41) | 1.31× lower at baseline in the lines without ADM2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with PTEN; also absent: CXADR, ARHGAP26, CFL1P1-1 |
| [[SEC24D]] | C | SEC24D's natural level strengthens GFPT1's drug response | SEC24D's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.12; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, -32.9); signed map (-51.3, 10.1). **Vector** length 159, 67.0% of its response variance represented; |z| ≥ 3 in 1,672 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.67 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.67 to 16); *protein secretion* (hallmark, mean cos +0.61 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.2 | -3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +6.2 | -6.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +6.2 | +7.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.9 | -6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +3.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +4.7 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | -0.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.2 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -11.1 | -11.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.7 | -15.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -9.0 | -7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -8.9 | -11.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -8.3 | -7.3 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.8 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | glutamine--fructose-6-phosphate transaminase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:69,319,780-69,387,250 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GFAT, GFA, GFAT1; previously GFPT |
| Gene groups (HGNC) | Glutamine--fructose-6-phosphate transaminase family |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 12 pathways, smallest: Synthesis of UDP-N-acetyl-glucosamine; Diseases associated with glycosylation precursor biosynthesis; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06210](https://www.uniprot.org/uniprotkb/Q06210) (Glutamine--fructose-6-phosphate aminotransferase):

> Rate-limiting enzyme of the hexosamine biosynthetic pathway (HBP) that catalyzes the formation of glucosamine-6-phosphate from fructose-6-phosphate and glutamine, thereby controlling the flux of glucose into this pathway. Inhibited by UDP-N-acetylglucosamine (UDP-GlcNAc) through a feedback loop. Fine-tunes the metabolic fluctuations of UDP-GlcNAc and its impacts on hyaluronan synthesis during tissue remodeling. Via control of the HPB, regulates the availability of precursors for N- and O-linked …

**Summary**, from NCBI Gene [2673](https://www.ncbi.nlm.nih.gov/gene/2673):

> This gene encodes the first and rate-limiting enzyme of the hexosamine pathway and controls the flux of glucose into the hexosamine pathway. The product of this gene catalyzes the formation of glucosamine 6-phosphate. [provided by RefSeq, Sep 2008]

**Accessions** — [HGNC:4241](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4241) · Entrez [2673](https://www.ncbi.nlm.nih.gov/gene/2673) · UniProt [Q06210](https://www.uniprot.org/uniprotkb/Q06210) · Ensembl [ENSG00000198380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198380)

## Data

Gene col 12581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12581); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12581]; `tensor/DDL_lfc|DDL_z.npy` [12581]; `embed/gene_vectors.npy` [12581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12581 or target_col == 12581). Every well: [[GFPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GFPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
