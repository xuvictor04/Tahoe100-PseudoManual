---
symbol: "STK39"
type: "gene"
col: 12635
ensembl_id: "ENSG00000198648"
name: "serine/threonine kinase 39"
location: "2q24.3"
module: 59
arm: "-"
pooled_cpm: 152.92
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# STK39

*serine/threonine kinase 39* — 2q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.30× (z +4.3, q 0.009, up in 26 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Bexarotene (drug)]] 0.05 µM: 1.25× (z +3.7, q 0.052, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 5 µM in 2 lines (A498 3.67×, SW 900 4.13×); [[Clobetasol propionate (drug)]] 0.5 µM in 2 lines (A498 3.27×, SW 900 3.66×); [[Budesonide (drug)]] 5 µM in 2 lines (A498 3.10×, SW 900 3.87×).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.318× (z -19.0, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FARP1]] (+0.67, fdr 7e-06), [[ASAP2]] (+0.65, fdr 7e-06), [[SRPK1]] (+0.64, fdr 7e-06); moves opposite to [[ARMCX1]] (-0.56, fdr 3e-05), [[TBC1D17]] (-0.54, fdr 1e-05), [[DCP1A]] (-0.54, fdr 2e-05).
> It sits in the **-** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SCEL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12635.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Clobetasol propionate (drug)]] 5 µM in 2 lines (A498 3.67×, SW 900 4.13×); [[Clobetasol propionate (drug)]] 0.5 µM in 2 lines (A498 3.27×, SW 900 3.66×); [[Budesonide (drug)]] 5 µM in 2 lines (A498 3.10×, SW 900 3.87×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.30×** | +4.3 | 0.009 | 26/47 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Bexarotene (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.052 | 23/47 (HT-29, BT-474, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.21× | +3.2 | 0.23 | 21/47 (A498, SW 900, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.21× | +3.1 | 0.23 | 17/47 (SNU-423, SW480, …) | top dose only |  |
| [[Bexarotene (drug)]] 5 µM |  | 1.20× | +3.0 | 0.23 | 21/47 (HT-29, LS 180, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12635.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.318×** | -19.0 | 0e+00 | 47/47 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.321×** | -18.8 | 0e+00 | 46/47 (KATO III, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.458×** | -18.3 | 0e+00 | 38/47 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.348×** | -17.5 | 0e+00 | 46/47 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.472×** | -12.0 | 7e-31 | 40/46 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.663×** | -9.6 | 6e-20 | 38/47 (SW48, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.554×** | -9.4 | 4e-19 | 34/47 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.582×** | -9.0 | 2e-17 | 37/47 (NCI-H23, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -8.4 | 4e-15 | 30/48 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -7.9 | 2e-13 | 40/48 (NCI-H23, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.668×** | -6.7 | 1e-09 | 30/47 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.671×** | -6.6 | 2e-09 | 31/47 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -6.3 | 1e-08 | 30/47 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.685×** | -6.3 | 1e-08 | 30/47 (HepG2/C3A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.714×** | -5.2 | 9e-06 | 26/44 (A-427, Panc 03.27, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -4.7 | 8e-05 | 26/47 (C32, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.742×** | -4.5 | 3e-04 | 27/47 (HepG2/C3A, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12635. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 99.2 | 15 | 5 | [[Clobetasol propionate (drug)]] 0.05 µM 3.83× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.8) |
| [[SW 900 (line)]] | alt | 184 | 12 | 4 | [[Clobetasol propionate (drug)]] 5 µM 4.13× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -13.6) |
| [[COLO 205 (line)]] | alt | 439 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0381× (z -27.7) |
| [[C32 (line)]] | wt | 134 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -19.4) |
| [[SW48 (line)]] | wt | 332 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -21.0) |
| [[KATO III (line)]] | alt | 265 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0734× (z -25.9) |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 11 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.138× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 689 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -24.4) |
| [[NCI-H1573 (line)]] | alt | 105 | 4 | 6 (1 ⚠) | [[Clobetasol propionate (drug)]] 5 µM 2.54× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 146 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.6) |
| [[LoVo (line)]] | wt | 398 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.137× (z -19.4) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -23.4) |
| [[SW1417 (line)]] | alt | 360 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -18.7) |
| [[LOX-IMVI (line)]] | wt | 156 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -23.0) |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -13.7) |
| [[BT-474 (line)]] | alt | 136 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 61.0 | 2 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +16.1) | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -13.5) |
| [[RKO (line)]] | wt | 155 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.221× (z -17.0) |
| [[A-427 (line)]] | wt | 108 | 0 | 6 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.265× (z -15.8) |
| [[HT-29 (line)]] | alt | 332 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.164× (z -16.9) |
| [[NCI-H23 (line)]] | alt | 126 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -27.7) |
| [[A549 (line)]] | wt | 161 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.112× (z -23.8) |
| [[HepG2_C3A (line)]] | wt | 293 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.8) |
| [[LS 180 (line)]] | wt | 266 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.125× (z -21.7) |
| [[NCI-H2030 (line)]] | alt | 183 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -15.0) |
| [[A-172 (line)]] | wt | 164 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.332× (z -11.1) |
| [[J82 (line)]] | alt | 116 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -18.4) |
| [[NCI-H1792 (line)]] | alt | 80.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -15.2) |
| [[C-33 A (line)]] | alt | 96.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -13.9) |
| [[HS-578T (line)]] | alt | 63.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -10.8) |
| [[SHP-77 (line)]] | alt | 100 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -14.4) |
| [[SW480 (line)]] | alt | 77.3 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.207× (z -21.7) |
| [[Hs 766T (line)]] | wt | 63.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -11.3) |
| [[HCT15 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.3) |
| [[HOP62 (line)]] | alt | 81.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.410× (z -9.0) |
| [[SNU-1 (line)]] | wt | 88.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.300× (z -9.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 50.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.351× (z -9.4) |
| [[AN3 CA (line)]] | alt | 112 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 81.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12635), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FARP1]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.65 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[SRPK1]] | +0.64 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TMEM181]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PKP4]] | +0.60 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[TLN2]] | +0.59 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[SLC26A2]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[THSD4]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[OSBPL10]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.58 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[IPO7]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CTPS1]] | +0.56 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMCX1]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[TBC1D17]] | -0.54 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[DCP1A]] | -0.54 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[MAF]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[KLC4]] | -0.52 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[CLIP3]] | -0.52 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[TP53BP1]] | -0.52 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PI4KB]] | -0.52 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[SAT2]] | -0.51 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[TRADD]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[IQUB]] | -0.50 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CIR1]] | -0.50 | -0.62 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCEL]] | B | SCEL activity raises STK39's level | lines that do not express SCEL (35) vs lines expressing it (15) | 1.84× lower at baseline in the lines without SCEL | 0.082 | ⚠ within organs, on part of the lines; also absent: FGFBP1, MUC4, DAPP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **-** arm (projection on the module's main direction -0.557). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (40.7, 7.9); signed map (7.8, 43.3). **Vector** length 119, 39.8% of its response variance represented; |z| ≥ 3 in 1,783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | +5.0 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | -0.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.7 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +3.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.3 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +0.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.4 | +1.5 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.6 | -9.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.5 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -7.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.2 | -12.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.2 | -2.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.3 — chr2:167,954,020-168,247,595 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DCHT, SPAK |
| Gene groups (HGNC) | OXSR1/STK39 kinase family |
| Hallmark sets | ANDROGEN_RESPONSE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UEW8](https://www.uniprot.org/uniprotkb/Q9UEW8) (STE20/SPS1-related proline-alanine-rich protein kinase):

> Effector serine/threonine-protein kinase component of the WNK-SPAK/OSR1 kinase cascade, which is involved in various processes, such as ion transport, response to hypertonic stress and blood pressure. Specifically recognizes and binds proteins with a RFXV motif. Acts downstream of WNK kinases (WNK1, WNK2, WNK3 or WNK4): following activation by WNK kinases, catalyzes phosphorylation of ion cotransporters, such as SLC12A1/NKCC2, SLC12A2/NKCC1, SLC12A3/NCC, SLC12A5/KCC2 or SLC12A6/KCC3, regulating …

**Summary**, from NCBI Gene [27347](https://www.ncbi.nlm.nih.gov/gene/27347):

> This gene encodes a serine/threonine kinase that is thought to function in the cellular stress response pathway. The kinase is activated in response to hypotonic stress, leading to phosphorylation of several cation-chloride-coupled cotransporters. The catalytically active kinase specifically activates the p38 MAP kinase pathway, and its interaction with p38 decreases upon cellular stress, suggesting that this kinase may serve as an intermediate in the response to cellular stress. [provided by …

**Accessions** — [HGNC:17717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17717) · Entrez [27347](https://www.ncbi.nlm.nih.gov/gene/27347) · UniProt [Q9UEW8](https://www.uniprot.org/uniprotkb/Q9UEW8) · Ensembl [ENSG00000198648](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198648)

## Data

Gene col 12635: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12635); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12635, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12635]; `tensor/DDL_lfc|DDL_z.npy` [12635]; `embed/gene_vectors.npy` [12635]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12635 or target_col == 12635). Every well: [[STK39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
