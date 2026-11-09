---
symbol: "SEZ6L2"
type: "gene"
col: 10544
ensembl_id: "ENSG00000174938"
name: "seizure related 6 homolog like 2"
location: "16p11.2"
module: 3
arm: "+"
pooled_cpm: 42.99
n_lines_expressing: 44
n_dd_up: 4
n_dd_down: 16
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# SEZ6L2

*seizure related 6 homolog like 2* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.20× (z +7.8, q 4e-12, up in 36 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.77×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.403× (z -12.7, q 4e-34, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOSPD3]] (+0.74, fdr 7e-06), [[KDELR1]] (+0.73, fdr 7e-06), [[ADIPOR1]] (+0.72, fdr 7e-06); moves opposite to [[ZNF681]] (-0.69, fdr 1e-05), [[ZNF507]] (-0.66, fdr 1e-05), [[PPIL1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Docetaxel (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10544.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 3.77×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.20×** | +7.8 | 4e-12 | 36/40 (NCI-H1573, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +7.1 | 3e-10 | 30/35 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.63×** | +4.5 | 0.001 | 27/38 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +4.0 | 0.008 | 27/41 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.21 | 24/42 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.35× | +3.0 | 0.25 | 22/42 (SW 900, NCI-H1792, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.403×** | -12.7 | 4e-34 | 40/42 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.299×** | -11.9 | 4e-30 | 41/42 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.327×** | -10.6 | 6e-24 | 41/42 (NCI-H23, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.457×** | -7.7 | 2e-12 | 38/42 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.525×** | -6.3 | 3e-08 | 38/42 (LOX-IMVI, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.528×** | -6.3 | 3e-08 | 35/42 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.656×** | -4.1 | 0.003 | 29/42 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.659×** | -4.1 | 0.003 | 28/42 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.679×** | -3.7 | 0.016 | 23/42 (HepG2/C3A, Hs 766T, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.695×** | -3.6 | 0.019 | 28/42 (HCT15, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.678×** | -3.5 | 0.021 | 29/42 (SW1417, A498, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.687×** | -3.5 | 0.023 | 27/41 (LOX-IMVI, HOP62, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.711×** | -3.2 | 0.052 | 17/41 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.721×** | -3.2 | 0.052 | 25/41 (SW 1271, SW 900, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.718×** | -3.0 | 0.098 | 21/42 (SW 1088, SW1417, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.737×** | -3.0 | 0.098 | 22/42 (HT-29, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -10.0) |
| [[H4 (line)]] | wt | 57.0 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.138× (z -10.9) |
| [[HOP62 (line)]] | alt | 47.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -12.6) |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.9) |
| [[LOX-IMVI (line)]] | wt | 20.5 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.122× (z -11.2) |
| [[LS 180 (line)]] | wt | 32.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -10.5) |
| [[NCI-H2030 (line)]] | alt | 80.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 34.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -8.9) |
| [[PANC-1 (line)]] | alt | 64.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -14.1) |
| [[SW1417 (line)]] | alt | 84.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -14.1) |
| [[CFPAC-1 (line)]] | alt | 41.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -10.9) |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -12.0) |
| [[J82 (line)]] | alt | 27.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.6) |
| [[KATO III (line)]] | alt | 31.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 48.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -10.8) |
| [[NCI-H23 (line)]] | alt | 30.8 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0974× (z -14.3) |
| [[SHP-77 (line)]] | alt | 150 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.5) |
| [[SW 900 (line)]] | alt | 52.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -13.6) |
| [[A-427 (line)]] | wt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 83.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 60.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.6) |
| [[Hs 766T (line)]] | wt | 43.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.237× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.77× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.216× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 23.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -11.3) |
| [[RKO (line)]] | wt | 25.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.198× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 45.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.184× (z -10.0) |
| [[SNU-1 (line)]] | wt | 50.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -10.0) |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.248× (z -9.7) |
| [[SW480 (line)]] | alt | 22.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -8.8) |
| [[A498 (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.52 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.28 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOSPD3]] | +0.74 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[KDELR1]] | +0.73 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.72 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.71 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.70 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[PLD3]] | +0.70 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[CBFA2T2]] | +0.69 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[ALKBH7]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[KLHL7]] | +0.68 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[A1BG]] | +0.66 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[RAB40C]] | +0.66 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[MARK4]] | +0.66 | +0.64 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF681]] | -0.69 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.66 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.66 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[ST7L]] | -0.66 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.65 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[ATIC]] | -0.64 | -0.67 / -0.65 | both halves | 7e-06 |  |
| [[COA7]] | -0.63 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.63 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ELK4]] | -0.63 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.62 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[KICS2]] | -0.61 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[CPSF2]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Docetaxel (drug)]] 5 µM | C | SEZ6L2 activity lowers the cells' numbers under Docetaxel 5 µM (makes them more sensitive) | lines that do not express SEZ6L2 (6) vs lines expressing it (42) | the lines without SEZ6L2: 1.18× the cells of the other lines | 0.071 | ⚠ tissue-confounded; across organs; also absent: ASPHD1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.658). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (3.8, -15.0); signed map (-34.7, 13.4). **Vector** length 87.1, 26.7% of its response variance represented; |z| ≥ 3 in 619 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -2.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +0.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.6 | +2.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.7 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.0 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.9 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | seizure related 6 homolog like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,871,159-29,899,550 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSK-1, FLJ90517 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXD5](https://www.uniprot.org/uniprotkb/Q6UXD5) (Seizure 6-like protein 2):

> May contribute to specialized endoplasmic reticulum functions in neurons.

**Summary**, from NCBI Gene [26470](https://www.ncbi.nlm.nih.gov/gene/26470):

> This gene encodes a seizure-related protein that is localized on the cell surface. The gene is located in a region of chromosome 16p11.2 that is thought to contain candidate genes for autism spectrum disorders (ASD), though there is no evidence directly implicating this gene in ASD. Increased expression of this gene has been found in lung cancers, and the protein is therefore considered to be a novel prognostic marker for lung cancer. Alternative splicing of this gene results in multiple …

**Accessions** — [HGNC:30844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30844) · Entrez [26470](https://www.ncbi.nlm.nih.gov/gene/26470) · UniProt [Q6UXD5](https://www.uniprot.org/uniprotkb/Q6UXD5) · Ensembl [ENSG00000174938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174938)

## Data

Gene col 10544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10544); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10544]; `tensor/DDL_lfc|DDL_z.npy` [10544]; `embed/gene_vectors.npy` [10544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10544 or target_col == 10544). Every well: [[SEZ6L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEZ6L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
