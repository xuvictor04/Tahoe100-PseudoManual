---
symbol: "PRDX5"
type: "gene"
col: 4733
ensembl_id: "ENSG00000126432"
name: "peroxiredoxin 5"
location: "11q13.1"
module: 42
arm: "+"
pooled_cpm: 29.11
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# PRDX5

*peroxiredoxin 5* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.17× (z +13.4, q 5e-38, up in 41 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.43× (z +4.1, q 0.005, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.99×, NCI-H460 5.64×, HEC-1-A 4.35×, NCI-H1792 6.65×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 4.17×, HEC-1-A 4.69×, KATO III 3.82×, A549 5.92×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.729× (z -5.1, q 2e-04, down in 26 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.316×, NCI-H2030 0.468×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0645×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0812×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEST1]] (+0.54, fdr 4e-05), [[OS9]] (+0.54, fdr 2e-05), [[CDC26]] (+0.52, fdr 2e-05); moves opposite to [[SRSF7]] (-0.50, fdr 2e-05), [[SRSF2]] (-0.49, fdr 3e-05), [[BRCA2]] (-0.43, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4733.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.99×, NCI-H460 5.64×, HEC-1-A 4.35×, NCI-H1792 6.65×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (PANC-1 4.17×, HEC-1-A 4.69×, KATO III 3.82×, A549 5.92×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.17×** | +13.4 | 5e-38 | 41/41 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +13.1 | 6e-37 | 33/35 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +7.7 | 2e-12 | 32/39 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.82×** | +7.0 | 5e-10 | 37/45 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.005 | 21/48 (LoVo, A-427, …) | top dose only |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.33× | +3.1 | 0.20 | 19/48 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | 1.32× | +3.0 | 0.20 | 15/48 (hTERT-HPNE, BT-474, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4733.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.316×, NCI-H2030 0.468×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0645×); [[Epirubicin (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0812×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.729×** | -5.1 | 2e-04 | 26/47 (BT-474, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.63 | 15/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4733. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 25.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +9.9) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 26.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 28.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 31.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +11.5) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.82× (z +11.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 53.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.8) |
| [[PANC-1 (line)]] | alt | 49.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +13.4) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 23.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +9.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 30.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 43.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.8) |
| [[C32 (line)]] | wt | 18.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +8.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0645× (z -12.3) |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0812× (z -11.1) |
| [[HS-578T (line)]] | alt | 38.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +8.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +9.0) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +9.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.22× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 15.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.64× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 93.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4733), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEST1]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[OS9]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CDC26]] | +0.52 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[PLD3]] | +0.52 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[FKBP8]] | +0.51 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[PSAP]] | +0.51 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[C18orf32]] | +0.50 | +0.33 / +0.46 | both halves | 1e-04 |  |
| [[DAD1]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[COX7A2L]] | +0.48 | +0.32 / +0.53 | both halves | 1e-04 | pathway: Cellular response to chemical stress |
| [[SEL1L]] | +0.48 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[CALU]] | +0.48 | +0.53 / +0.38 | both halves | 7e-05 |  |
| [[GGCX]] | +0.48 | +0.39 / +0.44 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRSF7]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[SRSF2]] | -0.49 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[BRCA2]] | -0.43 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[DDX52]] | -0.42 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[ATRIP]] | -0.41 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[REXO5]] | -0.41 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[ANKRD26]] | -0.41 | -0.42 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (5.1, -30.2); signed map (-57.0, 5.3). **Vector** length 55.8, 10.1% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -0.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.1 | +0.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.8 | -1.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:64,318,121-64,321,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACR1, AOEB166, MGC142285, PRXV, PMP20, B166, PRDX6, PLP |
| Gene groups (HGNC) | Peroxiredoxins |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, HYPOXIA |
| Reactome | 6 pathways, smallest: Detoxification of Reactive Oxygen Species; TP53 Regulates Metabolic Genes; Cellular response to chemical stress |
| Matched by | ensembl_id |

**Function**, from UniProt [P30044](https://www.uniprot.org/uniprotkb/P30044) (Peroxiredoxin-5, mitochondrial):

> Thiol-specific peroxidase that catalyzes the reduction of hydrogen peroxide and organic hydroperoxides to water and alcohols, respectively. Plays a role in cell protection against oxidative stress by detoxifying peroxides and as sensor of hydrogen peroxide-mediated signaling events.

**Summary**, from NCBI Gene [25824](https://www.ncbi.nlm.nih.gov/gene/25824):

> This gene encodes a member of the peroxiredoxin family of antioxidant enzymes, which reduce hydrogen peroxide and alkyl hydroperoxides. The encoded protein interacts with peroxisome receptor 1 and plays an antioxidant protective role in different tissues under normal conditions and during inflammatory processes. The use of alternate transcription start sites is thought to result in transcript variants that use different in-frame translational start codons to generate isoforms that are targeted …

**Accessions** — [HGNC:9355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9355) · Entrez [25824](https://www.ncbi.nlm.nih.gov/gene/25824) · UniProt [P30044](https://www.uniprot.org/uniprotkb/P30044) · Ensembl [ENSG00000126432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126432)

## Data

Gene col 4733: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4733); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4733, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4733]; `tensor/DDL_lfc|DDL_z.npy` [4733]; `embed/gene_vectors.npy` [4733]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4733 or target_col == 4733). Every well: [[PRDX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRDX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
