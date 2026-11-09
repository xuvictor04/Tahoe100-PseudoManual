---
symbol: "AGRN"
type: "gene"
col: 11980
ensembl_id: "ENSG00000188157"
name: "agrin"
location: "1p36.33"
module: 138
arm: "+"
pooled_cpm: 78.29
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 15
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# AGRN

*agrin* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +6.0, q 1e-06, up in 27 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.425× (z -11.2, q 2e-26, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLXNB2]] (+0.66, fdr 7e-06), [[NFKB2]] (+0.65, fdr 7e-06), [[TTYH3]] (+0.64, fdr 8e-06); moves opposite to [[ZFYVE9]] (-0.63, fdr 1e-05), [[KIAA1143]] (-0.54, fdr 1e-05), [[RNF13]] (-0.54, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CDC42BPG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11980.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +6.0 | 1e-06 | 27/46 (AsPC-1, A498, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.028 | 24/47 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.8 | 0.028 | 25/47 (SNU-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.028 | 24/47 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.27× | +3.2 | 0.16 | 18/41 (Panc 03.27, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | 1.25× | +3.1 | 0.16 | 21/47 (A-172, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.27× | +3.1 | 0.16 | 18/41 (NCI-H2030, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11980.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.425×** | -11.2 | 2e-26 | 43/47 (HOP62, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.535×** | -8.7 | 1e-15 | 41/47 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -7.5 | 2e-11 | 40/47 (KATO III, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.373×** | -7.1 | 1e-10 | 37/43 (HOP62, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.637×** | -6.0 | 2e-07 | 38/48 (HOP62, SW 1088, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.685×** | -5.2 | 1e-05 | 30/47 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.687×** | -5.0 | 5e-05 | 31/45 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **0.755×** | -3.9 | 0.007 | 26/47 (NCI-H1573, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.771×** | -3.6 | 0.019 | 27/47 (SW 1088, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.773×** | -3.4 | 0.033 | 23/48 (NCI-H1573, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.790×** | -3.3 | 0.055 | 23/47 (SW48, J82, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.792×** | -3.2 | 0.056 | 22/47 (NCI-H1573, Hs 766T, …) | all doses, flat | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | 0.846× | -3.2 | 0.056 | 20/47 (CHP-212, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.729×** | -3.1 | 0.073 | 22/48 (HOP62, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **0.803×** | -3.0 | 0.084 | 21/47 (Panc 03.27, CHP-212, …) | inconsistent across doses | position effect removed |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.803×** | -3.0 | 0.084 | 20/46 (A549, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11980. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 168 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.2) | [[Bortezomib (drug)]] 0.05 µM 0.226× (z -14.4) |
| [[HT-29 (line)]] | alt | 185 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.244× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 54.6 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +11.6) | — |
| [[A498 (line)]] | wt | 78.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +14.5) | — |
| [[KATO III (line)]] | alt | 77.9 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.317× (z -11.0) |
| [[LoVo (line)]] | wt | 55.4 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 50.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +15.2) | — |
| [[LOX-IMVI (line)]] | wt | 50.6 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.306× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 63.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.5) | [[Bortezomib (drug)]] 0.05 µM 0.374× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 63.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 54.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.1) | [[Bortezomib (drug)]] 0.05 µM 0.431× (z -8.7) |
| [[SW 1088 (line)]] | alt | 105 | 0 | 2 | — | [[Altretamine (drug)]] 5 µM 0.0665× (z -10.2) |
| [[SW 900 (line)]] | alt | 87.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +13.5) | [[Bortezomib (drug)]] 0.05 µM 0.293× (z -9.9) |
| [[A-172 (line)]] | wt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.8) | — |
| [[A-427 (line)]] | wt | 38.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -11.9) |
| [[A549 (line)]] | wt | 80.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.355× (z -9.0) |
| [[BT-474 (line)]] | alt | 60.1 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.265× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 211 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.6) | — |
| [[H4 (line)]] | wt | 113 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.271× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 96.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.295× (z -9.2) |
| [[HS-578T (line)]] | alt | 103 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.360× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 57.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 65.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.319× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 103 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.357× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.152× (z -8.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 47.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.266× (z -8.7) |
| [[SNU-1 (line)]] | wt | 34.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 84.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[SW480 (line)]] | alt | 58.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.391× (z -8.8) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 92.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 82.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 63.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11980), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLXNB2]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_MYOGENESIS; STRING 512 |
| [[NFKB2]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[TTYH3]] | +0.64 | +0.66 / +0.58 | both halves | 8e-06 |  |
| [[DMWD]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[ZMIZ2]] | +0.62 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[ISYNA1]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[PLEC]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 494 |
| [[GET4]] | +0.61 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RMRP]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[BAHCC1]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SLC25A22]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[FGFRL1]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFYVE9]] | -0.63 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[KIAA1143]] | -0.54 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[RNF13]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[TOMM70]] | -0.53 | -0.49 / -0.54 | both halves | 1e-05 | pathway: SARS-CoV-2 Infection |
| [[PSMB5]] | -0.51 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD39]] | -0.51 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[FAM217B]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[GSTO1]] | -0.50 | -0.40 / -0.43 | both halves | 5e-05 | pathway: Metabolism of vitamins and cofactors |
| [[INVS]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[COA6]] | -0.50 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[IQCB1]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CACYBP]] | -0.50 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC42BPG]] | B | CDC42BPG activity raises AGRN's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 1.48× lower at baseline in the lines without CDC42BPG | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[SMAD3]] | B | SMAD3 activity raises AGRN's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without SMAD3 | 0.042 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[SYNPO]] | B | SYNPO activity raises AGRN's level | lines that do not express SYNPO (15) vs lines expressing it (35) | 1.49× lower at baseline in the lines without SYNPO | 0.046 | ⚠ within organs, on part of the lines; also absent: GLIS3, ENSG00000261227, ADAM7-AS1; maybe low, not absent |
| [[HLA-H]] | B | HLA-H activity raises AGRN's level | lines that do not express HLA-H (8) vs lines expressing it (42) | 1.73× lower at baseline in the lines without HLA-H | 0.071 | ⚠ within organs, on part of the lines; also absent: GPAT3, S100A6, ENSG00000290574; maybe low, not absent |
| [[SDC4]] | B | SDC4 activity raises AGRN's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 2.06× lower at baseline in the lines without SDC4 | 0.074 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[MUC5AC]] | B | MUC5AC activity raises AGRN's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 1.48× lower at baseline in the lines without MUC5AC | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[PLEC]] | C | PLEC activity raises AGRN's level | lines that do not express PLEC (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.0, -4.9); signed map (-6.9, 28.5). **Vector** length 139, 42.2% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +6.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +5.8 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.2 | +1.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +3.9 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +2.8 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.5 | +2.4 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +2.5 | +2.9 |
|  | [[Pentoxifylline (drug)]] 5 µM |  | +2.4 | +2.5 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -10.1 | -11.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -9.0 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.4 | -7.5 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -7.2 | -7.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -5.4 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -5.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -4.7 | -3.9 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -4.4 | -3.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.4 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | agrin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:1,020,120-1,056,118 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously AGRIN |
| Gene groups (HGNC) | Proteoglycans; SEA domain containing |
| Hallmark sets | MYOGENESIS, GLYCOLYSIS |
| Reactome | 43 pathways, smallest: Defective EXT1 causes exostoses 1, TRPS2 and CHDS; Defective EXT2 causes exostoses 2; Defective B3GALT6 causes EDSP2 and SEMDJL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [O00468](https://www.uniprot.org/uniprotkb/O00468) (Agrin):

> Depending on alternative splicing and post-translational modifications, it has a role in different processes, including neuromuscular junction formation and maintenance, and regulation of neurite outgrowth (By similarity). Also involved in positive regulation of cartilage formation through alpha-dystroglycan binding and up-regulation of SOX9.; [Isoform 1]: Heparan sulfate basal lamina glycoprotein that plays a central role in the formation and the maintenance of the neuromuscular junction (NMJ) …

**Summary**, from NCBI Gene [375790](https://www.ncbi.nlm.nih.gov/gene/375790):

> This gene encodes one of several proteins that are critical in the development of the neuromuscular junction (NMJ), as identified in mouse knock-out studies. The encoded protein contains several laminin G, Kazal type serine protease inhibitor, and epidermal growth factor domains. Additional post-translational modifications occur to add glycosaminoglycans and disulfide bonds. In one family with congenital myasthenic syndrome affecting limb-girdle muscles, a mutation in this gene was found. …

**Accessions** — [HGNC:329](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:329) · Entrez [375790](https://www.ncbi.nlm.nih.gov/gene/375790) · UniProt [O00468](https://www.uniprot.org/uniprotkb/O00468) · Ensembl [ENSG00000188157](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188157)

## Data

Gene col 11980: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11980); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11980, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11980]; `tensor/DDL_lfc|DDL_z.npy` [11980]; `embed/gene_vectors.npy` [11980]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11980 or target_col == 11980). Every well: [[AGRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
