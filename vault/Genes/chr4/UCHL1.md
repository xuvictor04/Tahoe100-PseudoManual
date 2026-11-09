---
symbol: "UCHL1"
type: "gene"
col: 7795
ensembl_id: "ENSG00000154277"
name: "ubiquitin C-terminal hydrolase L1"
location: "4p13"
module: 117
arm: "+"
pooled_cpm: 28.26
n_lines_expressing: 21
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# UCHL1

*ubiquitin C-terminal hydrolase L1* — 4p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 9.14× (z +19.0, q 0e+00, up in 17 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.43× (z +7.6, q 4e-12, up in 16 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.271×, A-427 0.326×, NCI-H23 0.312×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ME1]] (+0.57, fdr 1e-05), [[SLC7A11]] (+0.57, fdr 2e-05), [[AKR1B1]] (+0.56, fdr 1e-05); moves opposite to [[TPRN]] (-0.47, fdr 2e-04), [[MTRES1]] (-0.47, fdr 2e-04), [[GON4L]] (-0.46, fdr 8e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BEND6]] → it (grade B ⚠); 3 go from it, the strongest it → [[MAP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **9.14×** | +19.0 | 0e+00 | 17/17 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.63×** | +14.3 | 7e-44 | 16/16 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.34×** | +13.3 | 4e-38 | 15/17 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.43×** | +7.6 | 4e-12 | 16/18 (HOP62, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.37×** | +7.4 | 1e-11 | 18/18 (HOP62, A-427, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.31×** | +6.8 | 1e-09 | 17/19 (NCI-H23, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.5 | 8e-09 | 7/19 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +5.9 | 3e-07 | 17/19 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +5.7 | 6e-07 | 17/18 (HOP62, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.4 | 3e-06 | 7/18 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +4.9 | 5e-05 | 9/18 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +4.4 | 4e-04 | 11/18 (C-33 A, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **1.63×** | +4.0 | 0.003 | 11/18 (NCI-H1792, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.56×** | +3.8 | 0.005 | 8/17 (SNU-423, CHP-212, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.008 | 11/18 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.056 | 5/19 (A-172, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.271×, A-427 0.326×, NCI-H23 0.312×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 5 µM |  | 0.477× | -3.3 | 0.46 | 6/19 (NCI-H23, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 79.9 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.74× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 5.15× (z +11.9) | — |
| [[A-427 (line)]] | wt | 79.3 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.90× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 121 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.01× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 48.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.67× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 109 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.56× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.43× (z +8.9) | — |
| [[A498 (line)]] | wt | 38.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +12.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 59.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.5× (z +14.9) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 185 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.57× (z +10.2) | — |
| [[NCI-H1792 (line)]] | alt | 68.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.4× (z +14.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.64× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.98× (z +9.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 72.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.77× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 93.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.61× (z +8.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 127 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.24 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ME1]] | +0.57 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC7A11]] | +0.57 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[AKR1B1]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.55 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[MLLT11]] | +0.55 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[TXNRD1]] | +0.54 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[HSPB8]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[CTNNA1]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[MAP1B]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[CNN3]] | +0.53 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[PFN2]] | +0.53 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[B4GALNT1]] | +0.52 | +0.57 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPRN]] | -0.47 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[MTRES1]] | -0.47 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[GON4L]] | -0.46 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[FBXL12]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[CHKB]] | -0.44 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[ZNF200]] | -0.44 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[SELENOH]] | -0.44 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[TAF12]] | -0.44 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[GCAT]] | -0.44 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[ZNF415]] | -0.44 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[ZBTB48]] | -0.43 | -0.38 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEND6]] | B | BEND6 activity raises UCHL1's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 5.35× lower at baseline in the lines without BEND6 | 0.069 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ |
| [[MAP1B]] | C | MAP1B activity raises UCHL1's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 6.26× lower at baseline in the lines without MAP1B | 0.013 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL; co-absent with the target |
| [[PCDH10]] | C | PCDH10 activity raises UCHL1's level | lines that do not express PCDH10 (24) vs lines expressing it (26) | 5.87× lower at baseline in the lines without PCDH10 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TWIST1, PRR16, FMN2; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP4]] | B | UCHL1 activity raises MAP4's level | lines that do not express UCHL1 (29) vs lines expressing it (21) | 1.16× lower at baseline in the lines without UCHL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: NEFL, ADD2, CDH4 |
| [[TES]] | B | UCHL1 activity lowers TES's level | lines that do not express UCHL1 (29) vs lines expressing it (21) | 1.78× higher at baseline in the lines without UCHL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: NEFL, ADD2, CDH4 |
| [[PCDH10]] | C | UCHL1 activity raises PCDH10's level | lines that do not express UCHL1 (29) vs lines expressing it (21) | 3.55× lower at baseline in the lines without UCHL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: NEFL, ADD2, CDH4; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.6, 48.7); signed map (52.3, -11.7). **Vector** length 55.5, 17.0% of its response variance represented; |z| ≥ 3 in 395 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +7.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +6.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.3 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +0.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.9 | -1.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | +0.5 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -3.3 |
|  | [[Resveratrol (drug)]] 5 µM |  | -0.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin C-terminal hydrolase L1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p13 — chr4:41,256,413-41,268,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PGP9.5, Uch-L1, UCHL-1; previously PARK5 |
| Gene groups (HGNC) | Ubiquitin C-terminal hydrolases |
| Reactome | 2 pathways, smallest: UCH proteinases; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [P09936](https://www.uniprot.org/uniprotkb/P09936) (Ubiquitin carboxyl-terminal hydrolase isozyme L1):

> Deubiquitinase that plays a role in the regulation of several processes such as maintenance of synaptic function, cardiac function, inflammatory response or osteoclastogenesis. Abrogates the ubiquitination of multiple proteins including WWTR1/TAZ, EGFR, HIF1A and beta-site amyloid precursor protein cleaving enzyme 1/BACE1. In addition, recognizes and hydrolyzes a peptide bond at the C-terminal glycine of ubiquitin to maintain a stable pool of monoubiquitin that is a key requirement for the …

**Summary**, from NCBI Gene [7345](https://www.ncbi.nlm.nih.gov/gene/7345):

> The protein encoded by this gene belongs to the peptidase C12 family. This enzyme is a thiol protease that hydrolyzes a peptide bond at the C-terminal glycine of ubiquitin. This gene is specifically expressed in the neurons and in cells of the diffuse neuroendocrine system. Mutations in this gene may be associated with Parkinson disease.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:12513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12513) · Entrez [7345](https://www.ncbi.nlm.nih.gov/gene/7345) · UniProt [P09936](https://www.uniprot.org/uniprotkb/P09936) · Ensembl [ENSG00000154277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154277)

## Data

Gene col 7795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7795); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7795]; `tensor/DDL_lfc|DDL_z.npy` [7795]; `embed/gene_vectors.npy` [7795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7795 or target_col == 7795). Every well: [[UCHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
