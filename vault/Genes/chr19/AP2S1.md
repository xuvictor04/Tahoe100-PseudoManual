---
symbol: "AP2S1"
type: "gene"
col: 488
ensembl_id: "ENSG00000042753"
name: "adaptor related protein complex 2 subunit sigma 1"
location: "19q13.32"
module: 48
arm: "+"
pooled_cpm: 34.26
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# AP2S1

*adaptor related protein complex 2 subunit sigma 1* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.35× (z +7.4, q 6e-11, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 3.66×, A549 4.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 3.96×; ⚠ cell-cycle shift, explains ~41% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.552× (z -7.3, q 2e-10, down in 38 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SK-MEL-2 0.104×, RPMI-7951 0.253×, LOX-IMVI 0.343×, J82 0.376×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.176×, hTERT-HPNE 0.191×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.112×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (LOX-IMVI 0.259×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AP1S1]] (+0.74, fdr 7e-06), [[ANAPC11]] (+0.73, fdr 7e-06), [[COX6A1]] (+0.73, fdr 7e-06); moves opposite to [[ZXDA]] (-0.69, fdr 1e-04), [[GALNT7-DT]] (-0.68, fdr 5e-04), [[PSMD6-AS1]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EGFL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (A498 3.66×, A549 4.95×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 3.96×; ⚠ cell-cycle shift, explains ~41% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.35×** | +7.4 | 6e-11 | 42/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **2.34×** | +7.4 | 6e-11 | 38/44 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **2.16×** | +6.4 | 3e-08 | 32/37 (HOP62, A498, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **2.05×** | +6.2 | 7e-08 | 36/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.79×** | +5.0 | 6e-05 | 32/48 (SW480, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.69×** | +4.5 | 5e-04 | 34/46 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | **1.56×** | +3.9 | 0.009 | 27/47 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.53×** | +3.6 | 0.026 | 27/44 (NCI-H2030, SW480, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.2 | 0.077 | 22/46 (NCI-H2030, HT-29, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **1.49×** | +3.2 | 0.077 | 21/39 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 488.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (SK-MEL-2 0.104×, RPMI-7951 0.253×, LOX-IMVI 0.343×, J82 0.376×, …); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.176×, hTERT-HPNE 0.191×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.112×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (LOX-IMVI 0.259×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.552×** | -7.3 | 2e-10 | 38/47 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -5.6 | 5e-06 | 38/47 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.621× | -3.5 | 0.10 | 25/48 (LOX-IMVI, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | 0.478× | -3.3 | 0.10 | 30/47 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.482× | -3.3 | 0.10 | 28/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.499× | -3.1 | 0.15 | 26/48 (HCT15, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | 0.507× | -3.1 | 0.17 | 22/47 (LOX-IMVI, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 80.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 53.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -9.4) |
| [[A-427 (line)]] | wt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.8) |
| [[A498 (line)]] | wt | 54.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[A549 (line)]] | wt | 26.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.95× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | — |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -11.4) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 83.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.8) |
| [[J82 (line)]] | alt | 57.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 86.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -12.5) |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -20.8) |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.3) |
| [[SW480 (line)]] | alt | 27.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.96× (z +9.0) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S1]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HIV Infection; STRING 921 |
| [[ANAPC11]] | +0.73 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[COX6A1]] | +0.73 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[YIF1B]] | +0.72 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.70 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[SNRPD2]] | +0.69 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.69 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MICOS13]] | +0.69 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[NDUFA11]] ⚠ | +0.68 | +0.49 / +0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP5MJ]] | +0.68 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ELOB]] | +0.67 | +0.54 / +0.55 | both halves | 1e-05 | pathway: HIV Infection |
| [[TRAPPC1]] | +0.67 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[TMEM256]] | +0.67 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZXDA]] | -0.69 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[GALNT7-DT]] | -0.68 | -0.63 / -0.24 | both halves | 5e-04 |  |
| [[PSMD6-AS1]] | -0.66 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ST7L]] | -0.66 | -0.61 / -0.32 | both halves | 2e-04 |  |
| [[RFX3-DT]] | -0.65 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[LEKR1]] | -0.65 | -0.64 / -0.29 | both halves | 2e-04 |  |
| [[PPP3CB-AS1]] | -0.65 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[CCT6P3]] | -0.64 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[KRCC1]] | -0.64 | -0.69 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[PCNX4-DT]] | -0.64 | -0.61 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[TMEM202-AS1]] | -0.63 | -0.60 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[RAB30-DT]] | -0.63 | -0.64 / -0.21 | both halves | 7e-04 |  |
| [[ZXDB]] | -0.63 | -0.54 / -0.40 | both halves | 4e-05 |  |
| [[LINC02542]] | -0.63 | -0.59 / -0.22 | both halves | 6e-04 |  |
| [[RNF6]] | -0.63 | -0.61 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGFL7]] | B | EGFL7 activity lowers AP2S1's level | lines that do not express EGFL7 (9) vs lines expressing it (41) | 1.37× higher at baseline in the lines without EGFL7 | 0.071 | ⚠ within organs, on part of the lines; also absent: KCTD15 |
| [[HDAC6]] | B | HDAC6 activity lowers AP2S1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.3, -18.9); signed map (-35.6, 12.4). **Vector** length 79.8, 24.6% of its response variance represented; |z| ≥ 3 in 574 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytoprotection by HMOX1* (reactome, mean cos +0.51 to 9); *TP53 Regulates Metabolic Genes* (reactome, mean cos +0.52 to 10); *adipogenesis* (hallmark, mean cos +0.50 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.7 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.4 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +5.4 | +5.0 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +2.7 | +4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | -0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.3 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -7.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | +1.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 2 subunit sigma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:46,838,136-46,850,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBHOk, FBH3; previously CLAPS2, HHC3 |
| Gene groups (HGNC) | Adaptor related protein complex 2 |
| Hallmark sets | PROTEIN_SECRETION, UV_RESPONSE_UP |
| Reactome | 43 pathways, smallest: Nef Mediated CD8 Down-regulation; Nef Mediated CD4 Down-regulation; WNT5A-dependent internalization of FZD2, FZD5 and ROR2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P53680](https://www.uniprot.org/uniprotkb/P53680) (AP-2 complex subunit sigma):

> Component of the adaptor protein complex 2 (AP-2). Adaptor protein complexes function in protein transport via transport vesicles in different membrane traffic pathways. Adaptor protein complexes are vesicle coat components and appear to be involved in cargo selection and vesicle formation. AP-2 is involved in clathrin-dependent endocytosis in which cargo proteins are incorporated into vesicles surrounded by clathrin (clathrin-coated vesicles, CCVs) which are destined for fusion with the early …

**Summary**, from NCBI Gene [1175](https://www.ncbi.nlm.nih.gov/gene/1175):

> One of two major clathrin-associated adaptor complexes, AP-2, is a heterotetramer which is associated with the plasma membrane. This complex is composed of two large chains, a medium chain, and a small chain. This gene encodes the small chain of this complex. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:565) · Entrez [1175](https://www.ncbi.nlm.nih.gov/gene/1175) · UniProt [P53680](https://www.uniprot.org/uniprotkb/P53680) · Ensembl [ENSG00000042753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000042753)

## Data

Gene col 488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 488); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 488]; `tensor/DDL_lfc|DDL_z.npy` [488]; `embed/gene_vectors.npy` [488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 488 or target_col == 488). Every well: [[AP2S1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP2S1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
