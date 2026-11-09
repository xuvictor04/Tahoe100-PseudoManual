---
symbol: "PDK3"
type: "gene"
col: 875
ensembl_id: "ENSG00000067992"
name: "pyruvate dehydrogenase kinase 3"
location: "Xp22.11"
module: 99
arm: "+"
pooled_cpm: 111.93
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 35
n_dd_up_clean: 2
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PDK3

*pyruvate dehydrogenase kinase 3* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Pimitespib (drug)]] 0.05 µM: 1.40× (z +3.8, q 0.055, up in 35 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1792 3.39×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 3.32×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.40×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.183× (z -28.1, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM162A]] (+0.83, fdr 7e-06), [[INSIG2]] (+0.83, fdr 7e-06), [[PDK1]] (+0.82, fdr 7e-06); moves opposite to [[AVEN]] (-0.67, fdr 1e-05), [[PPP3CB-AS1]] (-0.65, fdr 3e-05), [[ITPA]] (-0.65, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 875.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H1792 3.39×); [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H1792 3.32×; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.40×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pimitespib (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.055 | 35/46 (HS-578T, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.055 | 28/47 (NCI-H460, KATO III, …) | top dose only | plate-row cell shift |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 1.22× | +3.4 | 0.13 | 20/46 (SW48, LOX-IMVI, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | 1.67× | +3.2 | 0.21 | 29/46 (COLO 205, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.31× | +3.1 | 0.25 | 21/47 (KATO III, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 875.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.183×** | -28.1 | 0e+00 | 46/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.228×** | -17.3 | 0e+00 | 46/46 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.233×** | -16.4 | 0e+00 | 46/46 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.371×** | -11.1 | 1e-26 | 42/45 (HepG2/C3A, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.381×** | -10.8 | 3e-25 | 38/41 (C32, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.554×** | -9.7 | 2e-20 | 41/47 (C32, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.442×** | -9.5 | 1e-19 | 42/47 (C32, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.587×** | -8.8 | 1e-16 | 44/46 (SNU-1, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -7.1 | 7e-11 | 39/43 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.593×** | -5.9 | 3e-07 | 39/45 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -5.7 | 6e-07 | 33/46 (C32, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.719×** | -5.4 | 3e-06 | 30/46 (C32, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.670×** | -4.7 | 1e-04 | 35/46 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.668×** | -4.5 | 3e-04 | 33/48 (C32, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.587×** | -4.3 | 6e-04 | 32/46 (PANC-1, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.687×** | -4.2 | 1e-03 | 31/45 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.707×** | -4.0 | 0.002 | 29/46 (hTERT-HPNE, CHP-212, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.725×** | -3.7 | 0.006 | 24/45 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.725×** | -3.7 | 0.006 | 30/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.726×** | -3.7 | 0.006 | 31/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 875. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 456 | 0 | 15 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0669× (z -38.7) |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -18.2) |
| [[Hs 766T (line)]] | wt | 268 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -22.5) |
| [[NCI-H1792 (line)]] | alt | 328 | 2 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -23.4) |
| [[SNU-423 (line)]] | alt | 151 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0453× (z -30.9) |
| [[MIA PaCa-2 (line)]] | alt | 137 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -27.2) |
| [[NCI-H2030 (line)]] | alt | 68.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -22.0) |
| [[CFPAC-1 (line)]] | alt | 97.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -24.1) |
| [[NCI-H460 (line)]] | wt | 130 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -33.0) |
| [[HCT15 (line)]] | alt | 159 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 162 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -22.8) |
| [[A549 (line)]] | wt | 112 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -21.3) |
| [[C-33 A (line)]] | alt | 238 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.7) |
| [[LOX-IMVI (line)]] | wt | 83.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 113 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -21.6) |
| [[PANC-1 (line)]] | alt | 55.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -22.8) |
| [[A-172 (line)]] | wt | 140 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -23.2) |
| [[COLO 205 (line)]] | alt | 188 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -15.8) |
| [[HEC-1-A (line)]] | alt | 74.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -23.7) |
| [[LS 180 (line)]] | wt | 116 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -15.1) |
| [[Panc 03.27 (line)]] | alt | 68.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -24.0) |
| [[RKO (line)]] | wt | 91.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -24.1) |
| [[SK-MEL-2 (line)]] | alt | 80.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.5) |
| [[SW1417 (line)]] | alt | 112 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.290× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.469× (z -10.1) |
| [[SW480 (line)]] | alt | 123 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -17.0) |
| [[A-427 (line)]] | wt | 87.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -22.0) |
| [[AN3 CA (line)]] | alt | 115 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.9) |
| [[H4 (line)]] | wt | 182 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0820× (z -23.8) |
| [[HepG2_C3A (line)]] | wt | 62.0 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0268× (z -22.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) |
| [[HT-29 (line)]] | alt | 28.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -15.5) |
| [[J82 (line)]] | alt | 94.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -17.7) |
| [[KATO III (line)]] | alt | 70.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -11.9) |
| [[SNU-1 (line)]] | wt | 120 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -24.0) |
| [[SW 900 (line)]] | alt | 87.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -16.1) |
| [[BT-474 (line)]] | alt | 177 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -10.0) |
| [[HOP62 (line)]] | alt | 99.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -21.2) |
| [[HS-578T (line)]] | alt | 83.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 53.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -14.1) |
| [[LoVo (line)]] | wt | 68.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 55.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.4) |
| [[SHP-77 (line)]] | alt | 118 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.5) |
| [[SW48 (line)]] | wt | 100 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -10.2) |
| [[SW 1088 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.5) |
| [[A498 (line)]] | wt | 26.1 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 875), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM162A]] | +0.83 | +0.90 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[INSIG2]] | +0.83 | +0.86 / +0.75 | both halves | 7e-06 |  |
| [[PDK1]] | +0.82 | +0.90 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_HYPOXIA; STRING 833 |
| [[HILPDA]] | +0.81 | +0.88 / +0.67 | both halves | 7e-06 |  |
| [[CDON]] | +0.80 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[HDAC3]] | +0.79 | +0.82 / +0.71 | both halves | 7e-06 | pathway: Signaling by Nuclear Receptors |
| [[HERC3]] | +0.78 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.78 | +0.85 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[WDR45B]] | +0.77 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[CABIN1]] | +0.77 | +0.82 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.67 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.65 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[ITPA]] | -0.65 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | -0.63 | -0.63 / -0.49 | both halves | 2e-05 |  |
| [[ANKLE2]] | -0.62 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[PARVA]] | -0.62 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[ZSCAN29]] | -0.61 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[FIZ1]] | -0.61 | -0.67 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PDK3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, -16.4); signed map (-35.8, 23.6). **Vector** length 150, 58.2% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.54 to 15); *Glycolysis* (reactome, mean cos +0.56 to 10); *Glucose metabolism* (reactome, mean cos +0.56 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +8.3 | +0.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.7 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.5 | -1.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.9 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.6 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | +1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.9 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.2 | -17.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.8 | -28.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.2 | -16.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -8.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -6.1 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.8 | -4.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:24,465,244-24,550,466 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pyruvate dehydrogenase kinase family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, GLYCOLYSIS, HYPOXIA |
| Reactome | 6 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Signaling by Retinoic Acid |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15120](https://www.uniprot.org/uniprotkb/Q15120) ([Pyruvate dehydrogenase (acetyl-transferring)] kinase isozyme 3, mitochondrial):

> Inhibits pyruvate dehydrogenase activity by phosphorylation of the E1 subunit PDHA1, and thereby regulates glucose metabolism and aerobic respiration. Can also phosphorylate PDHA2. Decreases glucose utilization and increases fat metabolism in response to prolonged fasting, and as adaptation to a high-fat diet. Plays a role in glucose homeostasis and in maintaining normal blood glucose levels in function of nutrient levels and under starvation. Plays a role in the generation of reactive oxygen …

**Summary**, from NCBI Gene [5165](https://www.ncbi.nlm.nih.gov/gene/5165):

> The pyruvate dehydrogenase (PDH) complex is a nuclear-encoded mitochondrial multienzyme complex that catalyzes the overall conversion of pyruvate to acetyl-CoA and CO(2). It provides the primary link between glycolysis and the tricarboxylic acid (TCA) cycle, and thus is one of the major enzymes responsible for the regulation of glucose metabolism. The enzymatic activity of PDH is regulated by a phosphorylation/dephosphorylation cycle, and phosphorylation results in inactivation of PDH. The …

**Accessions** — [HGNC:8811](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8811) · Entrez [5165](https://www.ncbi.nlm.nih.gov/gene/5165) · UniProt [Q15120](https://www.uniprot.org/uniprotkb/Q15120) · Ensembl [ENSG00000067992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067992)

## Data

Gene col 875: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 875); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 875, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 875]; `tensor/DDL_lfc|DDL_z.npy` [875]; `embed/gene_vectors.npy` [875]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 875 or target_col == 875). Every well: [[PDK3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDK3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
