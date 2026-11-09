---
symbol: "EHBP1"
type: "gene"
col: 3684
ensembl_id: "ENSG00000115504"
name: "EH domain binding protein 1"
location: "2p15"
module: 5
arm: "+"
pooled_cpm: 404.06
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 32
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# EHBP1

*EH domain binding protein 1* — 2p15

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 1.77×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 1.73×; ⚠ unreliable plate only).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.388× (z -23.6, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DIAPH2]] (+0.63, fdr 7e-06), [[SNRPB]] (+0.62, fdr 7e-06), [[ZRANB3]] (+0.60, fdr 1e-05); moves opposite to [[USP30]] (-0.62, fdr 1e-05), [[VPS37D]] (-0.58, fdr 1e-05), [[NISCH]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CASC19]] → it (grade B ⚠); 1 goes from it, the strongest it → [[RPAP3-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3684.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (Hs 766T 1.77×); [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H460 1.73×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Afatinib (drug)]] 0.5 µM |  | 1.15× | +3.3 | 0.32 | 13/49 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.32 | 21/48 (hTERT-HPNE, SW1417, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.32 | 19/48 (A-172, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3684.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.388×** | -23.6 | 0e+00 | 43/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.450×** | -14.1 | 2e-42 | 46/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.455×** | -13.4 | 2e-38 | 44/47 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -12.9 | 1e-35 | 42/48 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.513×** | -11.8 | 7e-30 | 47/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.521×** | -11.5 | 1e-28 | 44/48 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.549×** | -10.6 | 4e-24 | 39/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.561×** | -10.2 | 1e-22 | 44/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.561×** | -10.2 | 1e-22 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.566×** | -10.0 | 7e-22 | 39/48 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -9.3 | 8e-19 | 33/49 (SK-MEL-2, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.404×** | -8.3 | 3e-15 | 43/49 (KATO III, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.603×** | -8.2 | 8e-15 | 40/45 (NCI-H23, NCI-H1792, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -7.9 | 2e-13 | 36/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.665×** | -6.9 | 2e-10 | 38/47 (HepG2/C3A, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.780×** | -6.2 | 2e-08 | 31/48 (SNU-423, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.707×** | -6.1 | 3e-08 | 39/48 (MIA PaCa-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.717×** | -5.8 | 1e-07 | 38/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -4.6 | 1e-04 | 30/48 (CFPAC-1, SW48, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.783×** | -4.3 | 4e-04 | 28/48 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3684. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 927 | 0 | 22 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -24.0) |
| [[HepG2_C3A (line)]] | wt | 1,407 | 0 | 16 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -25.5) |
| [[MIA PaCa-2 (line)]] | alt | 854 | 0 | 15 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -22.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.389× (z -16.9) |
| [[PANC-1 (line)]] | alt | 405 | 0 | 15 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -22.2) |
| [[SW480 (line)]] | alt | 388 | 0 | 15 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -20.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.417× (z -20.2) |
| [[NCI-H460 (line)]] | wt | 258 | 1 (1 ⚠) | 13 (7 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.73× (z +8.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -20.5) |
| [[SK-MEL-2 (line)]] | alt | 497 | 0 | 14 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -25.8) |
| [[C32 (line)]] | wt | 762 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -23.5) |
| [[LOX-IMVI (line)]] | wt | 269 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -20.8) |
| [[NCI-H1792 (line)]] | alt | 547 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -29.9) |
| [[A-427 (line)]] | wt | 859 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -18.3) |
| [[HOP62 (line)]] | alt | 289 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -21.6) |
| [[NCI-H23 (line)]] | alt | 378 | 0 | 11 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.574× (z -12.1) |
| [[SW48 (line)]] | wt | 442 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -17.3) |
| [[A549 (line)]] | wt | 646 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 601 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -26.4) |
| [[LoVo (line)]] | wt | 215 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -20.2) |
| [[LS 180 (line)]] | wt | 409 | 0 | 9 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -16.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.374× (z -15.6) |
| [[A-172 (line)]] | wt | 399 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -20.4) |
| [[COLO 205 (line)]] | alt | 407 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -23.2) |
| [[H4 (line)]] | wt | 313 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.9) |
| [[HCT15 (line)]] | alt | 324 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.5) |
| [[HEC-1-A (line)]] | alt | 340 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -15.1) |
| [[NCI-H1573 (line)]] | alt | 287 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -21.0) |
| [[RPMI-7951 (line)]] | alt | 321 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.5) |
| [[SW1417 (line)]] | alt | 588 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -18.3) |
| [[A498 (line)]] | wt | 500 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -19.0) |
| [[BT-474 (line)]] | alt | 147 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.403× (z -10.0) |
| [[SNU-1 (line)]] | wt | 320 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.325× (z -13.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -10.2) |
| [[SNU-423 (line)]] | alt | 395 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -24.6) |
| [[hTERT-HPNE (line)]] | wt | 301 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.9) |
| [[Hs 766T (line)]] | wt | 233 | 1 | 2 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.77× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -10.5) |
| [[HS-578T (line)]] | alt | 253 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 307 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -17.8) |
| [[RKO (line)]] | wt | 230 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.388× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 408 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -10.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.486× (z -8.8) |
| [[C-33 A (line)]] | alt | 278 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.501× (z -9.7) |
| [[HT-29 (line)]] | alt | 246 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.500× (z -9.9) ⚠ toxic |
| [[J82 (line)]] | alt | 180 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.475× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 170 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.575× (z -8.8) |
| [[SHP-77 (line)]] | alt | 213 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.424× (z -12.1) |
| [[SW 1271 (line)]] | alt | 193 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.155× (z -10.2) |
| [[SW 900 (line)]] | alt | 220 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.0) |
| [[AN3 CA (line)]] | alt | 213 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 435 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 342 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 274 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3684), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH2]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SNRPB]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ZRANB3]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[PKP4]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[FAF1]] | +0.57 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[HDAC4]] | +0.57 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[DDX10]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MTAP]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[DOCK5]] | +0.54 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[DOCK1]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SNTB2]] | +0.53 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[TEAD1]] | +0.53 | +0.46 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[NISCH]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[LINC00674]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FBXO44]] | -0.53 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[FRG1DP]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[VAMP2]] | -0.52 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[DUSP11]] | -0.52 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[FN3K]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[PGAP3]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TP53TG1]] | -0.51 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[PRMT9]] | -0.51 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC19]] | B | CASC19 activity raises EHBP1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without CASC19 | 0.032 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPAP3-DT]] | C | EHBP1's natural level strengthens RPAP3-DT's drug response | EHBP1's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.05; direction not clear | 0.059 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.466). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-1.9, -33.0); signed map (4.6, -51.2). **Vector** length 93.4, 36.8% of its response variance represented; |z| ≥ 3 in 1,678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.1 | -3.0 |
|  | [[Busulfan (drug)]] 5 µM |  | +2.8 | +2.5 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.6 | +3.0 |
|  | [[Thymol (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.6 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.1 | -13.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.8 | -6.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | -5.9 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -5.1 | -8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.9 | -1.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | EH domain binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:62,673,851-63,046,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0903, NACSIN |
| Gene groups (HGNC) | NT-C2 domain containing; Bivalent Mical/EHBP Rab binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NDI1](https://www.uniprot.org/uniprotkb/Q8NDI1) (EH domain-binding protein 1):

> May play a role in actin reorganization. Links clathrin-mediated endocytosis to the actin cytoskeleton. May act as Rab effector protein and play a role in vesicle trafficking. Required for perinuclear sorting and insulin-regulated recycling of SLC2A4/GLUT4 in adipocytes (By similarity).

**Summary**, from NCBI Gene [23301](https://www.ncbi.nlm.nih.gov/gene/23301):

> This gene encodes an Eps15 homology domain binding protein. The encoded protein may play a role in endocytic trafficking. A single nucleotide polymorphism in this gene is associated with an aggressive form of prostate cancer. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Feb 2010]

**Accessions** — [HGNC:29144](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29144) · Entrez [23301](https://www.ncbi.nlm.nih.gov/gene/23301) · UniProt [Q8NDI1](https://www.uniprot.org/uniprotkb/Q8NDI1) · Ensembl [ENSG00000115504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115504)

## Data

Gene col 3684: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3684); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3684, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3684]; `tensor/DDL_lfc|DDL_z.npy` [3684]; `embed/gene_vectors.npy` [3684]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3684 or target_col == 3684). Every well: [[EHBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EHBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
