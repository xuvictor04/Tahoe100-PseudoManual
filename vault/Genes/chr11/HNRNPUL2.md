---
symbol: "HNRNPUL2"
type: "gene"
col: 13218
ensembl_id: "ENSG00000214753"
name: "heterogeneous nuclear ribonucleoprotein U like 2"
location: "11q12.3"
module: 22
arm: "+"
pooled_cpm: 117.83
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# HNRNPUL2

*heterogeneous nuclear ribonucleoprotein U like 2* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.52× (z +7.9, q 1e-12, up in 39 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW480 2.94×, PANC-1 2.25×, KATO III 2.20×, SW1417 2.24×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-172 2.81×, KATO III 2.43×, SW480 2.55×, PANC-1 2.25×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 2.34×, KATO III 1.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.725× (z -6.0, q 1e-06, down in 34 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.770× (z -5.1, q 1e-04, down in 32 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.424×, AsPC-1 0.447×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.441×, NCI-H2030 0.446×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.115×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP2R5D]] (+0.62, fdr 1e-05), [[CBX1]] (+0.58, fdr 1e-05), [[CKAP5]] (+0.55, fdr 3e-05); moves opposite to [[LINC00520]] (-0.53, fdr 3e-05), [[ABCA15P]] (-0.47, fdr 9e-05), [[NOP10]] (-0.47, fdr 4e-05, ⚠ NOP10 in the vector space only through flagged drug-doses), [[HDX]] (-0.47, fdr 4e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (SW480 2.94×, PANC-1 2.25×, KATO III 2.20×, SW1417 2.24×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (A-172 2.81×, KATO III 2.43×, SW480 2.55×, PANC-1 2.25×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-172 2.34×, KATO III 1.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.52×** | +7.9 | 1e-12 | 39/44 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.52×** | +7.6 | 1e-11 | 38/49 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.38×** | +6.3 | 7e-08 | 38/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.32×** | +5.0 | 8e-05 | 26/45 (A-172, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.40×** | +3.4 | 0.064 | 24/49 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.38×** | +3.3 | 0.085 | 23/47 (C32, RKO, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 0.424×, AsPC-1 0.447×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 2 lines (KATO III 0.441×, NCI-H2030 0.446×; ⚠ toxic); [[Lonafarnib (drug)]] 5 µM in 1 line (Panc 03.27 0.115×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -6.0 | 1e-06 | 34/47 (KATO III, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -5.1 | 1e-04 | 32/49 (NCI-H2347, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.796×** | -4.9 | 2e-04 | 30/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.784×** | -4.7 | 3e-04 | 26/48 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.791×** | -4.6 | 6e-04 | 34/49 (HOP62, HEC-1-A, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.825×** | -3.7 | 0.018 | 22/49 (H4, LOX-IMVI, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.840× | -3.3 | 0.088 | 21/48 (A-172, AN3 CA, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 123 | 3 (3 ⚠) | 3 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.81× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 160 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.43× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -12.1) ⚠ toxic |
| [[A498 (line)]] | wt | 72.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 98.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 90.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[PANC-1 (line)]] | alt | 123 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.25× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW480 (line)]] | alt | 133 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 97.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.11× (z +8.8) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H2030 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.446× (z -10.1) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.550× (z -9.8) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Panc 03.27 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.115× (z -14.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 139 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 196 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 74.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 126 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 120 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 111 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 141 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 76.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 105 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 93.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 145 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R5D]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CBX1]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CKAP5]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[INCENP]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[GTF3C1]] | +0.55 | +0.53 / +0.49 | both halves | 2e-05 |  |
| [[CDK5RAP2]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SF3B2]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[SPAG5]] | +0.54 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[USP48]] | +0.54 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SART1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MYH10]] | +0.54 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[DHX16]] | +0.53 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00520]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[ABCA15P]] | -0.47 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[NOP10]] ⚠ | -0.47 | -0.42 / -0.49 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HDX]] | -0.47 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[UPP1]] | -0.45 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[PHLDA2]] | -0.45 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[SPHK1]] | -0.45 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[GNG5]] | -0.43 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[NIPAL1]] | -0.43 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ROR1-AS1]] | -0.43 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[CRYM]] | -0.42 | -0.42 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.428). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.7, -53.1); signed map (-48.1, -32.8). **Vector** length 110, 31.1% of its response variance represented; |z| ≥ 3 in 695 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.2 | +3.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.2 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +0.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | +2.8 | +6.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[crizotinib (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +2.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.0 | -6.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -7.6 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -4.5 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.3 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | +0.3 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | heterogeneous nuclear ribonucleoprotein U like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,712,630-62,727,457 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762N1910; previously HNRPUL2 |
| Matched by | ensembl_id |

UniProt [Q1KMD3](https://www.uniprot.org/uniprotkb/Q1KMD3) carries no function annotation.

**Summary**, from NCBI Gene [221092](https://www.ncbi.nlm.nih.gov/gene/221092):

> Enables RNA binding activity. Predicted to be involved in alternative mRNA splicing, via spliceosome. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25451) · Entrez [221092](https://www.ncbi.nlm.nih.gov/gene/221092) · UniProt [Q1KMD3](https://www.uniprot.org/uniprotkb/Q1KMD3) · Ensembl [ENSG00000214753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214753)

## Data

Gene col 13218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13218); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13218]; `tensor/DDL_lfc|DDL_z.npy` [13218]; `embed/gene_vectors.npy` [13218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13218 or target_col == 13218). Every well: [[HNRNPUL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNRNPUL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
