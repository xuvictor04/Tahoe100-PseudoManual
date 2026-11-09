---
symbol: "GOSR2"
type: "gene"
col: 2946
ensembl_id: "ENSG00000108433"
name: "golgi SNAP receptor complex member 2"
location: "17q21.32"
module: 52
arm: "+"
pooled_cpm: 100.2
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# GOSR2

*golgi SNAP receptor complex member 2* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.98× (z +12.8, q 1e-34, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.684× (z -10.0, q 5e-21, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HM13]] (+0.77, fdr 7e-06), [[TICAM2]] (+0.76, fdr 7e-06), [[PMM2]] (+0.76, fdr 7e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +12.8 | 1e-34 | 44/48 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +10.7 | 4e-24 | 40/49 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.8 | 1e-06 | 28/48 (SW1417, A-427, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.26×** | +4.3 | 0.003 | 27/49 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.26×** | +4.1 | 0.004 | 25/48 (NCI-H460, HS-578T, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.9 | 0.011 | 0/50 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.19× | +3.2 | 0.11 | 21/48 (HEC-1-A, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.684×** | -10.0 | 5e-21 | 40/48 (SK-MEL-2, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.586×** | -10.0 | 5e-21 | 43/49 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -8.5 | 5e-15 | 30/44 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.656×** | -7.9 | 4e-13 | 34/48 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.650×** | -7.4 | 1e-11 | 31/45 (HCT15, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -6.5 | 6e-09 | 35/47 (Panc 03.27, J82, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.700×** | -6.4 | 1e-08 | 31/48 (A549, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.759×** | -5.2 | 2e-05 | 27/48 (H4, HepG2/C3A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.775×** | -4.8 | 1e-04 | 26/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.775×** | -4.6 | 2e-04 | 29/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.645×** | -4.3 | 9e-04 | 30/49 (C32, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.853× | -4.2 | 0.001 | 19/48 (AsPC-1, RKO, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **0.803×** | -4.1 | 0.002 | 24/48 (SW 900, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.658×** | -4.1 | 0.002 | 26/47 (HepG2/C3A, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.672×** | -3.9 | 0.004 | 21/38 (Panc 03.27, C32, …) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.846× | -3.1 | 0.060 | 19/48 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.853× | -3.0 | 0.087 | 19/48 (NCI-H460, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 107 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.63× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 100 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.423× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 128 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 108 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.514× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 103 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.42× (z +9.9) | [[Lonafarnib (drug)]] 5 µM 0.130× (z -11.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 89.9 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.42× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.508× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 116 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -16.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 51.3 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.47× (z +11.2) | [[Lonafarnib (drug)]] 5 µM 0.100× (z -10.7) ⚠ toxic |
| [[H4 (line)]] | wt | 176 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -10.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 91.4 | 2 | 1 | [[Auranofin (drug)]] 5 µM 3.25× (z +15.1) | [[Selinexor (drug)]] 5 µM 0.543× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.328× (z -10.0) |
| [[KATO III (line)]] | alt | 133 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.508× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 169 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -12.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 163 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 79.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.281× (z -14.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 76.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +12.7) | — |
| [[LOX-IMVI (line)]] | wt | 78.2 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.30× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -9.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 80.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +12.0) | — |
| [[NCI-H1573 (line)]] | alt | 169 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.02× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -17.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.383× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 132 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.56× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -18.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 128 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.55× (z +14.7) | [[Selinexor (drug)]] 5 µM 0.440× (z -13.6) |
| [[SW 1088 (line)]] | alt | 100 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0716× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0726× (z -9.7) |
| [[SW 900 (line)]] | alt | 96.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.68× (z +13.2) | — |
| [[A-172 (line)]] | wt | 106 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.31× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.145× (z -9.0) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -12.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 116 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.75× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 76.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.19× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 118 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -8.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 51.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 70.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +11.1) | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.106× (z -8.8) |
| [[PANC-1 (line)]] | alt | 55.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +10.2) | — |
| [[RKO (line)]] | wt | 92.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 151 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -16.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 72.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 73.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HM13]] | +0.77 | +0.72 / +0.85 | both halves | 7e-06 |  |
| [[TICAM2]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 |  |
| [[PMM2]] | +0.76 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[BET1L]] | +0.74 | +0.71 / +0.77 | both halves | 7e-06 | same gene group; pathway: Asparagine N-linked glycosylation; STRING 997 |
| [[SEC23IP]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 677 |
| [[TMED7-TICAM2]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PGM3]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[COL20A1]] | +0.71 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ZNF432]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[KDELR2]] | +0.71 | +0.65 / +0.79 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 576 |
| [[GOLGA3]] | +0.70 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GOSR2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers GOSR2's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.783). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (11.9, -28.8); signed map (-49.6, 6.8). **Vector** length 141, 46.7% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.9 | +12.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.3 | +4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +3.5 | +2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.7 | +1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -9.9 | -10.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.6 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.4 | -2.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.0 | -4.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -5.0 | -4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -4.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -3.2 | -2.7 |
|  | [[Afatinib (drug)]] 5 µM |  | -3.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | golgi SNAP receptor complex member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:46,923,075-46,975,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GS27, Bos1 |
| Gene groups (HGNC) | SNAREs; MicroRNA protein coding host genes |
| Hallmark sets | PROTEIN_SECRETION, UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 15 pathways, smallest: Cargo concentration in the ER; Intra-Golgi traffic; XBP1(S) activates chaperone genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O14653](https://www.uniprot.org/uniprotkb/O14653) (Golgi SNAP receptor complex member 2):

> Involved in transport of proteins from the cis/medial-Golgi to the trans-Golgi network.

**Summary**, from NCBI Gene [9570](https://www.ncbi.nlm.nih.gov/gene/9570):

> This gene encodes a trafficking membrane protein which transports proteins among the medial- and trans-Golgi compartments. Due to its chromosomal location and trafficking function, this gene may be involved in familial essential hypertension. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:4431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4431) · Entrez [9570](https://www.ncbi.nlm.nih.gov/gene/9570) · UniProt [O14653](https://www.uniprot.org/uniprotkb/O14653) · Ensembl [ENSG00000108433](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108433)

## Data

Gene col 2946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2946); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2946]; `tensor/DDL_lfc|DDL_z.npy` [2946]; `embed/gene_vectors.npy` [2946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2946 or target_col == 2946). Every well: [[GOSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
