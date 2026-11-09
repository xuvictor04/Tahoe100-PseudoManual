---
symbol: "CCDC124"
type: "gene"
col: 137
ensembl_id: "ENSG00000007080"
name: "coiled-coil domain containing 124"
location: "19p13.11"
module: 33
arm: "+"
pooled_cpm: 23.3
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# CCDC124

*coiled-coil domain containing 124* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.13× (z +13.0, q 1e-35, up in 41 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.05 µM: 1.55× (z +3.7, q 0.016, up in 31 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (SNU-423 0.246×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.167×; ⚠ toxic).
> Its strongest partners by |cos| (58 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 43 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FYCO1]] (+0.55, fdr 4e-04), [[TAMM41]] (+0.52, fdr 2e-04), [[PKN1]] (+0.51, fdr 0.001, ⚠ not reproduced), [[CFDP1]] (+0.50, fdr 6e-04); moves opposite to [[SNHG31]] (-0.50, fdr 4e-04), [[XNDC1N-ZNF705EP-ALG1L9P]] (-0.49, fdr 5e-04), [[KLHL15]] (-0.48, fdr 6e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **4.13×** | +13.0 | 1e-35 | 41/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **3.84×** | +11.8 | 8e-30 | 35/35 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.83×** | +8.7 | 9e-16 | 36/40 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +5.3 | 2e-05 | 32/44 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.75×** | +5.1 | 3e-05 | 35/48 (SW480, COLO 205, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.61×** | +4.4 | 0.001 | 34/46 (SW1417, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.57×** | +4.1 | 0.003 | 30/48 (SW480, COLO 205, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.52×** | +3.9 | 0.008 | 29/48 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.55×** | +3.7 | 0.016 | 31/47 (NCI-H460, SW480, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.82×** | +3.6 | 0.016 | 31/47 (HCT15, NCI-H2030, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.6 | 0.016 | 22/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.48×** | +3.6 | 0.016 | 24/47 (SW480, HCT15, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.018 | 25/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.48×** | +3.5 | 0.021 | 23/48 (LoVo, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.056 | 22/47 (NCI-H460, C-33 A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 137.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (SNU-423 0.246×; ⚠ cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.167×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.752× | -3.7 | 0.14 | 27/48 (MIA PaCa-2, SNU-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[C32 (line)]] | wt | 16.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.57× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[KATO III (line)]] | alt | 14.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.03× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 23.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LOX-IMVI (line)]] | wt | 30.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.42× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 24.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.97× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 30.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.71× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H2030 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.54× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 25.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-423 (line)]] | alt | 24.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Selinexor (drug)]] 5 µM 0.246× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 19.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.73× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 18.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.55× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 24.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HCT15 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.99× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[HEC-1-A (line)]] | alt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.90× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 35.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HT-29 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.44× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.42× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +9.1) ⚠ cell-cycle shift, explains ~90% of this change | — |
| [[Panc 03.27 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 48.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.167× (z -10.1) ⚠ toxic |
| [[SW1417 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 22 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FYCO1]] | +0.55 | +0.26 / +0.47 | both halves | 4e-04 |  |
| [[TAMM41]] | +0.52 | +0.31 / +0.33 | both halves | 2e-04 |  |
| [[PKN1]] | +0.51 | +0.15 / +0.42 | ⚠ not reproduced | 0.001 |  |
| [[CFDP1]] | +0.50 | +0.22 / +0.39 | both halves | 6e-04 |  |
| [[NAA10]] ⚠ | +0.50 | +0.31 / +0.40 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[METTL26]] | +0.50 | +0.12 / +0.41 | ⚠ not reproduced | 0.002 |  |
| [[NPPB]] | +0.49 | +0.36 / +0.36 | both halves | 1e-04 |  |
| [[TBC1D9B]] | +0.49 | +0.40 / +0.33 | both halves | 1e-04 |  |
| [[NF2]] | +0.48 | +0.47 / +0.30 | both halves | 2e-04 |  |
| [[RBFA]] | +0.48 | +0.24 / +0.38 | both halves | 5e-04 |  |
| [[SMS]] | +0.47 | +0.39 / +0.18 | ⚠ not reproduced | 9e-04 |  |
| [[BRD7]] | +0.47 | +0.35 / +0.29 | both halves | 2e-04 |  |
| [[NUDCD3]] | +0.47 | +0.31 / +0.33 | both halves | 2e-04 |  |
| [[SNX11]] | +0.46 | +0.34 / +0.28 | both halves | 3e-04 |  |
| [[VPS16]] | +0.46 | +0.34 / +0.39 | both halves | 1e-04 |  |
| [[FAM50A]] | +0.46 | +0.38 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG31]] | -0.50 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.49 | -0.24 / -0.25 | both halves | 5e-04 |  |
| [[KLHL15]] | -0.48 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[H2AZ1]] | -0.45 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[DNAJC22]] | -0.45 | -0.25 / -0.34 | both halves | 4e-04 |  |
| [[LINC01762]] | -0.45 | -0.11 / -0.22 | ⚠ not reproduced | 0.002 |  |
| [[SPART-AS1]] | -0.45 | -0.06 / -0.26 | ⚠ not reproduced | 0.004 |  |
| [[YTHDF3]] | -0.45 | -0.14 / -0.36 | ⚠ not reproduced | 0.002 |  |
| [[ALG1L9P]] | -0.44 | -0.17 / -0.22 | ⚠ not reproduced | 0.001 |  |
| [[MYLK4]] | -0.44 | -0.08 / -0.22 | ⚠ not reproduced | 0.003 |  |
| [[NCOA2]] | -0.43 | -0.30 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[RTCA-AS1]] | -0.42 | -0.17 / -0.28 | ⚠ not reproduced | 0.001 |  |
| [[KAZALD1]] | -0.42 | -0.31 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.270). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (15.2, -9.7); signed map (-24.3, -16.7). **Vector** length 47.6, 8.88% of its response variance represented; |z| ≥ 3 in 581 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +2.4 | +3.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +2.2 | +4.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.2 | +5.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.7 | +3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.9 | +1.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +0.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.3 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -0.8 | -1.1 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 124 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:17,933,015-17,943,991 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Lso2, oxs1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CT7](https://www.uniprot.org/uniprotkb/Q96CT7) (Coiled-coil domain-containing protein 124):

> Ribosome-binding protein involved in ribosome hibernation: associates with translationally inactive ribosomes and stabilizes the nonrotated conformation of the 80S ribosome, thereby promoting ribosome preservation and storage. Also required for proper progression of late cytokinetic stages.

**Summary**, from NCBI Gene [115098](https://www.ncbi.nlm.nih.gov/gene/115098):

> Enables RNA binding activity. Predicted to be involved in transcription by RNA polymerase II. Located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25171) · Entrez [115098](https://www.ncbi.nlm.nih.gov/gene/115098) · UniProt [Q96CT7](https://www.uniprot.org/uniprotkb/Q96CT7) · Ensembl [ENSG00000007080](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007080)

## Data

Gene col 137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 137); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 137]; `tensor/DDL_lfc|DDL_z.npy` [137]; `embed/gene_vectors.npy` [137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 137 or target_col == 137). Every well: [[CCDC124 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC124.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
