---
symbol: "MINDY2"
type: "gene"
col: 4933
ensembl_id: "ENSG00000128923"
name: "MINDY lysine 48 deubiquitinase 2"
location: "15q21.3-q22.1"
module: 41
arm: "+"
pooled_cpm: 250.1
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 42
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# MINDY2

*MINDY lysine 48 deubiquitinase 2* — 15q21.3-q22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 2.04×).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.457× (z -13.5, q 7e-39, down in 41 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.521× (z -12.2, q 7e-32, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL28]] (+0.74, fdr 7e-06), [[PLAG1]] (+0.73, fdr 7e-06), [[SRP54]] (+0.71, fdr 7e-06); moves opposite to [[PPP2CA]] (-0.70, fdr 7e-06), [[UTP20]] (-0.70, fdr 7e-06), [[CCT5]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TESK2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4933.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 2.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 5 µM |  | 1.16× | +4.0 | 0.035 | 13/49 (LOX-IMVI, SK-MEL-2, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.13× | +3.2 | 0.26 | 7/48 (hTERT-HPNE, HT-29, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.38× | +3.2 | 0.26 | 25/48 (CFPAC-1, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.12× | +3.1 | 0.27 | 8/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 1.12× | +3.0 | 0.27 | 2/48 (PANC-1, RKO) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 23 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.457×** | -13.5 | 7e-39 | 41/45 (NCI-H1792, A498, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **0.518×** | -12.3 | 3e-32 | 43/49 (AsPC-1, CFPAC-1, …) | all doses, flat | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.521×** | -12.2 | 7e-32 | 48/48 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.520×** | -11.8 | 9e-30 | 43/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.524×** | -11.6 | 5e-29 | 37/44 (SNU-1, AsPC-1, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -11.0 | 2e-26 | 36/49 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -10.2 | 2e-22 | 33/48 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.696×** | -9.5 | 9e-20 | 41/48 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.607×** | -9.3 | 9e-19 | 45/48 (A498, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.624×** | -8.8 | 9e-17 | 36/48 (NCI-H1792, HCT15, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -8.7 | 2e-16 | 38/48 (A498, H4, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.630×** | -8.6 | 4e-16 | 35/48 (A498, NCI-H1792, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -8.4 | 1e-15 | 43/48 (A498, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.625×** | -8.4 | 1e-15 | 39/47 (C32, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.638×** | -8.4 | 2e-15 | 43/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.730×** | -8.3 | 5e-15 | 30/48 (SNU-1, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.695×** | -6.5 | 2e-09 | 41/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.537×** | -6.1 | 3e-08 | 42/48 (CFPAC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.733×** | -5.4 | 1e-06 | 36/47 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.596×** | -5.0 | 1e-05 | 39/48 (SW 900, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -5.0 | 1e-05 | 31/48 (A498, H4, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.773×** | -4.8 | 4e-05 | 26/48 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.795×** | -4.2 | 4e-04 | 28/49 (PANC-1, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 344 | 0 | 20 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -20.4) |
| [[NCI-H2347 (line)]] | alt | 247 | 0 | 17 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -14.4) |
| [[NCI-H1792 (line)]] | alt | 434 | 0 | 16 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.263× (z -16.7) |
| [[MIA PaCa-2 (line)]] | alt | 506 | 0 | 14 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -24.5) |
| [[AsPC-1 (line)]] | alt | 380 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -12.6) |
| [[COLO 205 (line)]] | alt | 334 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.8) |
| [[HOP62 (line)]] | alt | 257 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.277× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.341× (z -12.3) |
| [[SNU-1 (line)]] | wt | 1,120 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -23.8) |
| [[CFPAC-1 (line)]] | alt | 442 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -21.1) |
| [[SW 900 (line)]] | alt | 219 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -14.7) |
| [[H4 (line)]] | wt | 235 | 0 | 10 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.298× (z -11.8) |
| [[SNU-423 (line)]] | alt | 207 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.440× (z -9.7) |
| [[A-172 (line)]] | wt | 189 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -12.0) |
| [[A549 (line)]] | wt | 290 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.4) |
| [[HCT15 (line)]] | alt | 335 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -13.3) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.424× (z -9.9) |
| [[Hs 766T (line)]] | wt | 447 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -12.7) |
| [[HT-29 (line)]] | alt | 208 | 0 | 8 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 220 | 0 | 8 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.275× (z -13.9) |
| [[KATO III (line)]] | alt | 341 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 331 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.513× (z -8.5) |
| [[HS-578T (line)]] | alt | 179 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -11.7) |
| [[J82 (line)]] | alt | 190 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.441× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.532× (z -8.7) |
| [[C32 (line)]] | wt | 196 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.351× (z -12.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.448× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 348 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 150 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -12.3) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.368× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 397 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.365× (z -12.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.505× (z -12.3) |
| [[LS 180 (line)]] | wt | 233 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW1417 (line)]] | alt | 172 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 181 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.499× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.524× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 159 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.538× (z -12.0) |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -9.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.483× (z -8.7) |
| [[AN3 CA (line)]] | alt | 134 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.268× (z -8.9) |
| [[BT-474 (line)]] | alt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.0) |
| [[C-33 A (line)]] | alt | 144 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 152 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.388× (z -10.1) |
| [[LoVo (line)]] | wt | 217 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.454× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 259 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.401× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change |
| [[SW 1088 (line)]] | alt | 222 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0610× (z -14.5) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW48 (line)]] | wt | 233 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.363× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 87.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 210 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 122 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 289 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL28]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PLAG1]] | +0.73 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[SRP54]] | +0.71 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.71 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[CDK2AP2]] | +0.71 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CDKN2D]] | +0.70 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[ANG]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[AFTPH]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[TULP3]] | +0.69 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[ARL3]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2CA]] | -0.70 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[UTP20]] | -0.70 | -0.69 / -0.66 | both halves | 7e-06 |  |
| [[CCT5]] | -0.70 | -0.66 / -0.71 | both halves | 7e-06 |  |
| [[ABCF2]] | -0.69 | -0.71 / -0.61 | both halves | 7e-06 |  |
| [[PSME3]] | -0.68 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[PSMD11]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[ZNF300]] | -0.66 | -0.48 / -0.67 | both halves | 2e-05 |  |
| [[PSMD1]] | -0.66 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[GRWD1]] | -0.66 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[WDR77]] | -0.65 | -0.68 / -0.61 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.65 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[TMEM33]] | -0.65 | -0.67 / -0.66 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TESK2]] | C | TESK2 activity lowers MINDY2's level | lines that do not express TESK2 (3) vs lines expressing it (46) | 2.19× higher at baseline in the lines without TESK2 | 0.081 | ⚠ few lines (3 vs 46); across organs; also absent: SYNPO2, SLC9A3, SFXN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.0, -34.0); signed map (-25.0, 14.8). **Vector** length 136, 53.1% of its response variance represented; |z| ≥ 3 in 1,849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +7.0 | -7.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +6.1 | -8.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +6.1 | -8.6 |
|  | [[Terfenadine (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.7 | +1.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.6 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.6 | -0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +3.5 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -9.6 | -12.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.9 | -8.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.4 | -9.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.7 | -8.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.8 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -6.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.4 | -5.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -5.0 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | MINDY lysine 48 deubiquitinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3-q22.1 — chr15:58,771,192-58,861,900 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1164; previously FAM63B |
| Gene groups (HGNC) | MINDY deubiquitinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBR6](https://www.uniprot.org/uniprotkb/Q8NBR6) (Ubiquitin carboxyl-terminal hydrolase MINDY-2):

> Deubiquitinase that can remove 'Lys-48'- and 'Lys-63'-linked conjugated ubiquitin from proteins. Acts as an inhibitor of TNF-induced RIPK1-mediated cell death by mediating deubiquitination of 'ys-612' of RIPK1, thereby impairing the interaction between RIPK1 and TNFR1 (TNFR1A or TNFR1B), and formation of TNF-R1 signaling complex (By similarity). Binds to polyubiquitin chains of different linkage types, including 'Lys-6', 'Lys-11', 'Lys-29', 'Lys-33', 'Lys-48' and 'Lys-63'.

**Summary**, from NCBI Gene [54629](https://www.ncbi.nlm.nih.gov/gene/54629):

> Enables peptidase activity and polyubiquitin modification-dependent protein binding activity. Predicted to be involved in chromatin remodeling and proteolysis. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26954](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26954) · Entrez [54629](https://www.ncbi.nlm.nih.gov/gene/54629) · UniProt [Q8NBR6](https://www.uniprot.org/uniprotkb/Q8NBR6) · Ensembl [ENSG00000128923](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128923)

## Data

Gene col 4933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4933); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4933]; `tensor/DDL_lfc|DDL_z.npy` [4933]; `embed/gene_vectors.npy` [4933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4933 or target_col == 4933). Every well: [[MINDY2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINDY2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
