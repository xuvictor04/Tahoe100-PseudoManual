---
symbol: "MLPH"
type: "gene"
col: 3704
ensembl_id: "ENSG00000115648"
name: "melanophilin"
location: "2q37.3"
module: 174
arm: "+"
pooled_cpm: 85.56
n_lines_expressing: 37
n_dd_up: 1
n_dd_down: 35
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 9
direction_downstream: 21
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# MLPH

*melanophilin* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Sapanisertib (drug)]] 0.05 µM: 1.36× (z +4.2, q 0.014, up in 22 of 35 measured lines) ⚠ cell-cycle shift, explains ~44% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.45×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.175× (z -35.3, q 0e+00, down in 34 of 35 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PYGB]] (+0.53, fdr 3e-05), [[HPCAL1]] (+0.48, fdr 3e-05), [[ENTPD6]] (+0.47, fdr 1e-04); moves opposite to [[TMEM52B]] (-0.50, fdr 5e-05), [[IL32]] (-0.50, fdr 2e-05), [[LINC02384]] (-0.48, fdr 6e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ITGB3]] → it (grade B ⚠); 21 go from it, the strongest it → [[NIBAN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3704.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.45×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.36×** | +4.2 | 0.014 | 22/35 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.18× | +3.3 | 0.24 | 12/35 (HT-29, Panc 03.27, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 17 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3704.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.175×** | -35.3 | 0e+00 | 34/35 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.372×** | -20.0 | 0e+00 | 33/36 (RPMI-7951, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.239×** | -18.7 | 0e+00 | 33/35 (HOP62, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.276×** | -18.4 | 0e+00 | 32/35 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.342×** | -15.3 | 0e+00 | 32/35 (KATO III, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.359×** | -14.6 | 0e+00 | 33/35 (COLO 205, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.388×** | -13.5 | 8e-40 | 33/35 (COLO 205, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.458×** | -10.2 | 1e-22 | 29/35 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.505×** | -9.7 | 1e-20 | 33/35 (NCI-H1792, HOP62, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.535×** | -8.9 | 3e-17 | 31/35 (HOP62, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.568×** | -8.1 | 4e-14 | 24/35 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.556×** | -7.6 | 1e-12 | 29/35 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.687×** | -7.6 | 2e-12 | 28/35 (J82, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.589×** | -7.5 | 2e-12 | 27/35 (HOP62, NCI-H1792, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.598×** | -7.3 | 9e-12 | 29/35 (HOP62, COLO 205, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -7.2 | 2e-11 | 30/36 (HOP62, NCI-H1792, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.595×** | -7.0 | 9e-11 | 26/35 (HOP62, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -6.6 | 1e-09 | 23/35 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.731×** | -6.3 | 9e-09 | 23/35 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.673×** | -5.6 | 5e-07 | 23/35 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -4.9 | 2e-05 | 21/35 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.003 | 15/36 (Panc 03.27, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3704. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 305 | 0 | 19 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0778× (z -34.4) |
| [[KATO III (line)]] | alt | 106 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -23.4) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0751× (z -29.5) |
| [[NCI-H1792 (line)]] | alt | 191 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -21.1) |
| [[RPMI-7951 (line)]] | alt | 254 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0936× (z -31.6) |
| [[A498 (line)]] | wt | 84.5 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 67.2 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -31.5) |
| [[COLO 205 (line)]] | alt | 409 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.126× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -15.1) |
| [[LoVo (line)]] | wt | 37.5 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -17.7) |
| [[LS 180 (line)]] | wt | 99.1 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.9) |
| [[H4 (line)]] | wt | 92.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0348× (z -28.8) |
| [[A549 (line)]] | wt | 118 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -23.2) |
| [[C32 (line)]] | wt | 33.4 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0531× (z -17.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.2) |
| [[PANC-1 (line)]] | alt | 79.0 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -26.2) |
| [[SNU-423 (line)]] | alt | 335 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -27.6) |
| [[CFPAC-1 (line)]] | alt | 108 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -22.6) |
| [[HT-29 (line)]] | alt | 167 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -19.0) |
| [[hTERT-HPNE (line)]] | wt | 51.0 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 59.1 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.0) |
| [[Hs 766T (line)]] | wt | 72.8 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -24.8) |
| [[J82 (line)]] | alt | 96.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0717× (z -25.5) |
| [[NCI-H1573 (line)]] | alt | 104 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -21.6) |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -18.8) |
| [[SW 900 (line)]] | alt | 194 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -21.9) |
| [[BT-474 (line)]] | alt | 227 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -20.5) |
| [[HS-578T (line)]] | alt | 38.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.3) |
| [[NCI-H2347 (line)]] | alt | 51.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -18.6) |
| [[AsPC-1 (line)]] | alt | 58.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -20.9) |
| [[SW48 (line)]] | wt | 41.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0263× (z -20.4) |
| [[HCT15 (line)]] | alt | 36.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.280× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 24.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.6) |
| [[SW1417 (line)]] | alt | 23.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -14.3) |
| [[SW 1088 (line)]] | alt | 106 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -8.6) |
| [[SW 1271 (line)]] | alt | 52.2 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0579× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 19.5 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.31 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.68 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 75.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.83 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.39 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3704), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PYGB]] | +0.53 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[HPCAL1]] | +0.48 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ENTPD6]] | +0.47 | +0.56 / +0.32 | both halves | 1e-04 |  |
| [[SLC17A9]] | +0.46 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[TRIB2]] | +0.46 | +0.49 / +0.44 | both halves | 3e-05 | same gene group |
| [[ITGB3]] | +0.46 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[TGM2]] | +0.46 | +0.46 / +0.39 | both halves | 5e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[RPS6KA2]] | +0.45 | +0.36 / +0.36 | both halves | 1e-04 | same gene group; pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[NIBAN2]] | +0.44 | +0.52 / +0.40 | both halves | 5e-05 |  |
| [[LINC02813]] | +0.44 | +0.38 / +0.46 | both halves | 6e-05 |  |
| [[VGF]] | +0.43 | +0.42 / +0.30 | both halves | 2e-04 |  |
| [[COL6A3]] | +0.43 | +0.44 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM52B]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[IL32]] | -0.50 | -0.46 / -0.46 | both halves | 2e-05 |  |
| [[LINC02384]] | -0.48 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[MED13]] | -0.47 | -0.47 / -0.36 | both halves | 1e-04 |  |
| [[NKX3-1]] | -0.45 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[GBP3]] | -0.45 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[NMI]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[APH1B]] | -0.45 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[PSME2]] | -0.44 | -0.49 / -0.41 | both halves | 4e-05 | same gene group |
| [[GBP1]] | -0.44 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CCL5]] | -0.44 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[SLC2A6]] | -0.44 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB3]] | B | ITGB3 activity raises MLPH's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without ITGB3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[SH3BP2]] | B | SH3BP2 activity raises MLPH's level | lines that do not express SH3BP2 (8) vs lines expressing it (42) | 2.88× lower at baseline in the lines without SH3BP2 | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity raises MLPH's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 4.47× lower at baseline in the lines without ITGA3 | 0.036 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises MLPH's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.26× lower at baseline in the lines without GBP1 | 0.040 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[TOP2A]] | B | TOP2A activity raises MLPH's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNFAIP6]] | B | TNFAIP6 activity raises MLPH's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without TNFAIP6 | 0.068 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF |
| [[RPS6KA2]] | B | RPS6KA2 activity raises MLPH's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without RPS6KA2 | 0.082 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[GBP3]] | C | GBP3 activity raises MLPH's level | lines that do not express GBP3 (11) vs lines expressing it (39) | 5.63× lower at baseline in the lines without GBP3 | 0.007 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3; co-absent with the target |
| [[PYGB]] | C | PYGB activity raises MLPH's level | lines that do not express PYGB (3) vs lines expressing it (47) | 6.74× lower at baseline in the lines without PYGB | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |

### Downstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 20, C 1. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIBAN2]] | B | MLPH activity raises NIBAN2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 3.07× lower at baseline in the lines without MLPH | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[NIBAN2]] | B | MLPH activity strengthens NIBAN2's drug response | lines that do not express MLPH (9) vs lines expressing it (35) | the lines without MLPH respond 0.67× as strongly (z diff +2.40); strongest at Panobinostat 5 µM: 0.79x vs 0.39x (z diff +5.2) | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32; target measured in part of the lines; artifact flags |
| [[TPCN1]] | B | MLPH activity raises TPCN1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without MLPH | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[PACSIN2]] | B | MLPH activity raises PACSIN2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without MLPH | 0.019 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[GBP1]] | B | MLPH activity raises GBP1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 3.44× lower at baseline in the lines without MLPH | 0.023 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[RPS6KA2]] | B | MLPH activity raises RPS6KA2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without MLPH | 0.032 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ITGA3]] | B | MLPH activity raises ITGA3's level | lines that do not express MLPH (13) vs lines expressing it (37) | 3.20× lower at baseline in the lines without MLPH | 0.033 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[NCOA1]] | B | MLPH activity lowers NCOA1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.41× higher at baseline in the lines without MLPH | 0.041 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ROBO2]] | B | MLPH activity lowers ROBO2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.89× higher at baseline in the lines without MLPH | 0.049 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ZFHX4-AS1]] | B | MLPH activity lowers ZFHX4-AS1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.68× higher at baseline in the lines without MLPH | 0.063 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[PSMB8]] | B | MLPH activity raises PSMB8's level | lines that do not express MLPH (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without MLPH | 0.064 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[ERGIC1]] | B | MLPH activity raises ERGIC1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without MLPH | 0.069 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.430). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (27.8, 4.5); signed map (4.9, 51.2). **Vector** length 91.7, 27.4% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.9 | -1.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | +3.8 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | -1.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | -0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | -0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | -0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | -6.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +0.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.9 | -7.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -10.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -2.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.1 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | melanophilin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:237,485,428-237,555,322 (+) |
| Ensembl biotype | protein_coding |
| Also known as | l1Rk3, l(1)-3Rk, Slac-2a, ln, exophilin-3, SLAC2-A |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Regulation of MITF-M-dependent genes involved in pigmentation; MITF-M-dependent gene expression; MITF-M-regulated melanocyte development |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BV36](https://www.uniprot.org/uniprotkb/Q9BV36) (Melanophilin):

> Rab effector protein involved in melanosome transport. Serves as link between melanosome-bound RAB27A and the motor protein MYO5A.

**Summary**, from NCBI Gene [79083](https://www.ncbi.nlm.nih.gov/gene/79083):

> This gene encodes a member of the exophilin subfamily of Rab effector proteins. The protein forms a ternary complex with the small Ras-related GTPase Rab27A in its GTP-bound form and the motor protein myosin Va. A similar protein complex in mouse functions to tether pigment-producing organelles called melanosomes to the actin cytoskeleton in melanocytes, and is required for visible pigmentation in the hair and skin. A mutation in this gene results in Griscelli syndrome type 3, which is …

**Accessions** — [HGNC:29643](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29643) · Entrez [79083](https://www.ncbi.nlm.nih.gov/gene/79083) · UniProt [Q9BV36](https://www.uniprot.org/uniprotkb/Q9BV36) · Ensembl [ENSG00000115648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115648)

## Data

Gene col 3704: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3704); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3704, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3704]; `tensor/DDL_lfc|DDL_z.npy` [3704]; `embed/gene_vectors.npy` [3704]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3704 or target_col == 3704). Every well: [[MLPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
