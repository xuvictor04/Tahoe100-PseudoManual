---
symbol: "SCHIP1"
type: "gene"
col: 7584
ensembl_id: "ENSG00000151967"
name: "schwannomin interacting protein 1"
location: "3q25.33"
module: 151
arm: "+"
pooled_cpm: 29.34
n_lines_expressing: 43
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 23
direction_downstream: 5
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# SCHIP1

*schwannomin interacting protein 1* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 1.50× (z +4.9, q 5e-04, up in 21 of 40 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.29× (z +4.4, q 0.003, up in 22 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.395× (z -11.2, q 3e-26, down in 34 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IQCJ-SCHIP1]] (+0.88, fdr 7e-06, ⚠ same locus), [[LINC01204]] (+0.67, fdr 7e-06), [[RDUR]] (+0.66, fdr 7e-06), [[CD44]] (+0.66, fdr 7e-06); moves opposite to [[DYNC2LI1]] (-0.62, fdr 1e-05), [[USP30]] (-0.60, fdr 1e-05), [[ARNT]] (-0.57, fdr 2e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[BNC2]] → it (grade B ⚠); 5 go from it, the strongest it → [[TEAD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7584.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.50×** | +4.9 | 5e-04 | 21/40 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.48×** | +4.7 | 7e-04 | 28/41 (NCI-H1573, SW480, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.4 | 0.003 | 22/41 (NCI-H2347, A-427, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.39×** | +4.0 | 0.009 | 18/41 (A-172, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.36×** | +3.5 | 0.049 | 16/40 (NCI-H1573, NCI-H23, …) | rises with dose | position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.059 | 15/41 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 1.30× | +3.2 | 0.11 | 12/41 (A549, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.28× | +3.0 | 0.19 | 12/40 (A-172, SNU-423, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7584.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.395×** | -11.2 | 3e-26 | 34/41 (LOX-IMVI, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.451×** | -9.6 | 3e-19 | 31/41 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.650×** | -7.3 | 5e-11 | 31/41 (RKO, HOP62, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -6.8 | 2e-09 | 25/41 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.575×** | -6.4 | 2e-08 | 23/38 (RKO, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.595×** | -6.2 | 4e-08 | 22/36 (LOX-IMVI, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.638×** | -5.0 | 5e-05 | 18/36 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.671×** | -4.8 | 1e-04 | 24/41 (HOP62, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.671×** | -4.5 | 4e-04 | 20/40 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.698×** | -4.3 | 9e-04 | 24/40 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.510×** | -4.2 | 0.001 | 21/39 (PANC-1, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.716×** | -4.0 | 0.003 | 20/40 (hTERT-HPNE, NCI-H1573, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.721×** | -3.9 | 0.004 | 19/41 (HOP62, H4, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.727×** | -3.8 | 0.005 | 19/38 (NCI-H2030, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.727×** | -3.8 | 0.005 | 15/41 (NCI-H1573, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.740×** | -3.6 | 0.011 | 15/41 (H4, NCI-H460, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.753×** | -3.4 | 0.021 | 16/40 (H4, NCI-H1573, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.033 | 17/40 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.034 | 16/41 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7584. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 47.8 | 0 | 10 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.568× (z -16.4) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.247× (z -11.5) |
| [[RKO (line)]] | wt | 62.0 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.117× (z -16.7) |
| [[LOX-IMVI (line)]] | wt | 51.3 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -16.1) |
| [[PANC-1 (line)]] | alt | 25.0 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.251× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 43.4 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -14.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 92.4 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -11.0) |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 7.92× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Adagrasib (drug)]] 0.05 µM 0.562× (z -9.6) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 23.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.281× (z -10.9) |
| [[A-427 (line)]] | wt | 37.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HEC-1-A (line)]] | alt | 36.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -9.0) |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -9.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 43.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.246× (z -9.7) |
| [[J82 (line)]] | alt | 100 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 21.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.107× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 5 µM 0.204× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 35.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.256× (z -9.3) |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.126× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -10.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.1 | 0 | 1 | — | [[Binimetinib (drug)]] 0.5 µM 0.152× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Panc 03.27 (line)]] | alt | 33.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.136× (z -11.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.125× (z -11.4) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A-172 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.31 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7584), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCJ-SCHIP1]] | +0.88 | +0.86 / +0.89 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01204]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[RDUR]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[CD44]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[RPSAP52]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SLC4A7]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[UBASH3B]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[BACH1]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[MAMLD1]] | +0.65 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[MIR100HG]] | +0.65 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[MARCHF4]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[NEK10]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[AMOTL1]] | +0.63 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2LI1]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[USP30]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[ARNT]] | -0.57 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[FPGT]] | -0.55 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CRYZL1]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[PICK1]] | -0.55 | -0.48 / -0.52 | both halves | 2e-05 | pathway: HALLMARK_MYOGENESIS |
| [[C12orf76]] | -0.54 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[PREPL]] | -0.54 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NISCH]] | -0.53 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[MAPKAPK5-AS1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[TRAPPC11]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[PIGB]] | -0.53 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 21, C 2. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BNC2]] | B | BNC2 activity raises SCHIP1's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 2.99× lower at baseline in the lines without BNC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182 |
| [[ADAMTS6]] | B | ADAMTS6 activity raises SCHIP1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.63× lower at baseline in the lines without ADAMTS6 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2 |
| [[FLI1]] | B | FLI1 activity raises SCHIP1's level | lines that do not express FLI1 (31) vs lines expressing it (19) | 2.45× lower at baseline in the lines without FLI1 | 0.025 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, LINC01615 |
| [[ADAMTS6]] | B | ADAMTS6 activity strengthens SCHIP1's drug response | lines that do not express ADAMTS6 (19) vs lines expressing it (22) | the lines without ADAMTS6 respond 0.62× as strongly (z diff +1.96); strongest at Dinaciclib 0.5 µM: 0.70x vs 0.44x (z diff +3.4) | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; target measured in part of the lines; artifact flags |
| [[KISS1]] | B | KISS1 activity strengthens SCHIP1's drug response | lines that do not express KISS1 (31) vs lines expressing it (10) | the lines without KISS1 respond 0.56× as strongly (z diff +1.83); strongest at Topotecan (hydrochloride) 5 µM: 0.64x vs 0.32x (z diff +4.1) | 0.036 | ⚠ within organs, on part of the lines; also absent: SIM1, CALB1, PSG1; target measured in part of the lines; artifact flags |
| [[FRMD4A]] | B | FRMD4A activity raises SCHIP1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.41× lower at baseline in the lines without FRMD4A | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6 |
| [[LTBP2]] | B | LTBP2 activity raises SCHIP1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without LTBP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[HHIP]] | B | HHIP activity raises SCHIP1's level | lines that do not express HHIP (33) vs lines expressing it (17) | 1.87× lower at baseline in the lines without HHIP | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL5A1, PLPP4, LINC01411; maybe low, not absent |
| [[MIR100HG]] | B | MIR100HG activity raises SCHIP1's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 2.81× lower at baseline in the lines without MIR100HG | 0.061 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2 |
| [[PDCD1LG2]] | B | PDCD1LG2 activity raises SCHIP1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without PDCD1LG2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[WNT5B]] | B | WNT5B activity raises SCHIP1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.72× lower at baseline in the lines without WNT5B | 0.064 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[BNC2]] | B | BNC2 activity strengthens SCHIP1's drug response | lines that do not express BNC2 (14) vs lines expressing it (27) | the lines without BNC2 respond 0.60× as strongly (z diff +1.39); strongest at Topotecan (hydrochloride) 5 µM: 0.69x vs 0.46x (z diff +2.7) | 0.065 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; target measured in part of the lines; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TEAD1]] | B | SCHIP1 activity raises TEAD1's level | lines that do not express SCHIP1 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without SCHIP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: DYRK3, IQCJ-SCHIP1, ROBO3 |
| [[IQCJ-SCHIP1]] | C | SCHIP1's natural level strengthens IQCJ-SCHIP1's drug response | SCHIP1's natural level across 41 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.55; direction not clear | 0.021 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IQCJ-SCHIP1]] | C | SCHIP1 activity raises IQCJ-SCHIP1's level | lines that do not express SCHIP1 (7) vs lines expressing it (43) | 5.26× lower at baseline in the lines without SCHIP1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DYRK3, IQCJ-SCHIP1, ROBO3; co-absent with the target; its own permutation p |
| [[MAMLD1]] | C | SCHIP1 activity raises MAMLD1's level | lines that do not express SCHIP1 (7) vs lines expressing it (43) | 4.62× lower at baseline in the lines without SCHIP1 | 0.089 | ⚠ within organs, on part of the lines; also absent: DYRK3, IQCJ-SCHIP1, ROBO3; co-absent with the target; its own permutation p |
| [[GJC1]] | C | SCHIP1 activity raises GJC1's level | lines that do not express SCHIP1 (7) vs lines expressing it (43) | 6.22× lower at baseline in the lines without SCHIP1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DYRK3, IQCJ-SCHIP1, ROBO3; co-absent with the target |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.825). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.5, 10.2); signed map (14.2, 46.2). **Vector** length 121, 33.5% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | +0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +1.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.8 | -7.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.8 | -4.3 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -4.1 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.5 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | schwannomin interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33 — chr3:159,273,244-159,897,629 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCHIP-1 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Hallmark sets | UV_RESPONSE_DN, MYOGENESIS |
| Matched by | ensembl_id |

UniProt [P0DPB3](https://www.uniprot.org/uniprotkb/P0DPB3) carries no function annotation.

**Summary**, from NCBI Gene [29970](https://www.ncbi.nlm.nih.gov/gene/29970):

> Enables identical protein binding activity. Predicted to be involved in positive regulation of hippo signaling. Predicted to act upstream of or within several processes, including face morphogenesis; fibroblast migration; and luteinization. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:15678](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15678) · Entrez [29970](https://www.ncbi.nlm.nih.gov/gene/29970) · UniProt [P0DPB3](https://www.uniprot.org/uniprotkb/P0DPB3) · Ensembl [ENSG00000151967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151967)

## Data

Gene col 7584: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7584); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7584, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7584]; `tensor/DDL_lfc|DDL_z.npy` [7584]; `embed/gene_vectors.npy` [7584]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7584 or target_col == 7584). Every well: [[SCHIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCHIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
