---
symbol: "ACAT1"
type: "gene"
col: 1108
ensembl_id: "ENSG00000075239"
name: "acetyl-CoA acetyltransferase 1"
location: "11q22.3"
module: 17
arm: "+"
pooled_cpm: 38.18
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ACAT1

*acetyl-CoA acetyltransferase 1* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.23× (z +21.9, q 0e+00, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +6.4, q 1e-08, up in 30 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.306×); [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (SW 1271 0.0699×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0868×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MATR3]] (+0.58, fdr 1e-05), [[GTF3A]] (+0.57, fdr 1e-05, ⚠ GTF3A in the vector space only through flagged drug-doses), [[ZDHHC17]] (+0.56, fdr 5e-05), [[QDPR]] (+0.56, fdr 1e-05); moves opposite to [[PRKD2]] (-0.53, fdr 2e-05), [[SLC25A44]] (-0.53, fdr 6e-04), [[NECTIN2]] (-0.50, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CFL2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1108.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.23×** | +21.9 | 0e+00 | 36/37 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.02×** | +19.2 | 0e+00 | 42/44 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +14.0 | 4e-42 | 38/42 (LoVo, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.32×** | +7.3 | 4e-11 | 29/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +6.4 | 1e-08 | 30/48 (NCI-H2347, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.32×** | +5.3 | 9e-06 | 24/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.32×** | +5.3 | 9e-06 | 27/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +5.1 | 2e-05 | 19/48 (A-172, SNU-423, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +5.0 | 4e-05 | 23/48 (KATO III, HT-29, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.30×** | +4.9 | 5e-05 | 22/47 (LoVo, A549, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.27×** | +4.5 | 4e-04 | 22/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +4.3 | 8e-04 | 16/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.25×** | +4.3 | 8e-04 | 22/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.012 | 19/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.4 | 0.022 | 13/33 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.4 | 0.027 | 12/48 (NCI-H2347, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1108.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 0.306×); [[Phenytoin (sodium) (drug)]] 0.05 µM in 1 line (SW 1271 0.0699×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (CHP-212 0.0868×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ivermectin (drug)]] 5 µM |  | 0.848× | -3.2 | 0.45 | 9/48 (LoVo, SW 1088, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1108. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 56.5 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +13.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 84.0 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.94× (z +13.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 46.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 38.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.65× (z +19.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 30.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +13.1) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 26.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +11.8) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 45.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +12.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 56.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 66.4 | 0 | 3 (1 ⚠) | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0699× (z -9.6) |
| [[SW480 (line)]] | alt | 46.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.19× (z +15.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 32.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.54× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 56.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +12.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 38.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 38.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.46× (z +10.3) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 31.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.70× (z +8.8) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.07× (z +10.3) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 36.9 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0868× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.54× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.12× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 60.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.306× (z -11.6) |
| [[SW 900 (line)]] | alt | 22.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +9.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 60.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1108), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MATR3]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GTF3A]] ⚠ | +0.57 | +0.60 / +0.49 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZDHHC17]] | +0.56 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[QDPR]] | +0.56 | +0.56 / +0.57 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[SEC22C]] | +0.55 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[DOCK7]] | +0.55 | +0.32 / +0.53 | both halves | 2e-04 |  |
| [[IARS2]] | +0.54 | +0.31 / +0.57 | both halves | 2e-04 | pathway: Mitochondrial protein degradation |
| [[NELFCD]] | +0.54 | +0.46 / +0.44 | both halves | 3e-05 | STRING 403 |
| [[DDHD2]] | +0.53 | +0.25 / +0.56 | both halves | 4e-04 |  |
| [[DCAF17]] | +0.53 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[CDC73]] | +0.52 | +0.22 / +0.53 | both halves | 6e-04 |  |
| [[IMPACT]] | +0.52 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[MCCC2]] | +0.52 | +0.67 / +0.48 | both halves | 2e-05 | pathway: Branched-chain amino acid catabolism; STRING 478 |

## Genes that move opposite

*25 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKD2]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[SLC25A44]] | -0.53 | -0.22 / -0.55 | both halves | 6e-04 | pathway: Branched-chain amino acid catabolism |
| [[NECTIN2]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MON1B]] | -0.49 | -0.31 / -0.57 | both halves | 2e-04 |  |
| [[ATG101]] | -0.48 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[TTLL3]] | -0.48 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[ARPC5L]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[FRMD8]] | -0.47 | -0.55 / -0.43 | both halves | 4e-05 |  |
| [[DMPK]] | -0.47 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[POLR2J4]] | -0.47 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[FBXL18]] | -0.46 | -0.23 / -0.48 | both halves | 5e-04 |  |
| [[PITPNA]] | -0.46 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CFL2]] | C | CFL2 activity raises ACAT1's level | lines that do not express CFL2 (4) vs lines expressing it (45) | 2.16× lower at baseline in the lines without CFL2 | 0.060 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: TPST1, SLC35F1, ITGA2B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.342). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-30.2, -15.4); signed map (-2.1, -37.4). **Vector** length 66.2, 12.2% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +19.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +21.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +14.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +3.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.8 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.2 | +0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.2 | -1.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.3 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.3 | -0.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | acetyl-CoA acetyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,116,695-108,147,603 (+) |
| Ensembl biotype | protein_coding |
| Also known as | THIL; previously ACAT |
| Gene groups (HGNC) | Acetyl-CoA acetyltransferases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 12 pathways, smallest: Utilization of Ketone Bodies; Synthesis of Ketone Bodies; Ketone body metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P24752](https://www.uniprot.org/uniprotkb/P24752) (Acetyl-CoA acetyltransferase, mitochondrial):

> This is one of the enzymes that catalyzes the last step of the mitochondrial beta-oxidation pathway, an aerobic process breaking down fatty acids into acetyl-CoA. Using free coenzyme A/CoA, catalyzes the thiolytic cleavage of medium- to long-chain 3-oxoacyl-CoAs into acetyl-CoA and a fatty acyl-CoA shortened by two carbon atoms. The activity of the enzyme is reversible and it can also catalyze the condensation of two acetyl-CoA molecules into acetoacetyl-CoA. Thereby, it plays a major role in …

**Summary**, from NCBI Gene [38](https://www.ncbi.nlm.nih.gov/gene/38):

> This gene encodes a mitochondrially localized enzyme that catalyzes the reversible formation of acetoacetyl-CoA from two molecules of acetyl-CoA. Defects in this gene are associated with 3-ketothiolase deficiency, an inborn error of isoleucine catabolism characterized by urinary excretion of 2-methyl-3-hydroxybutyric acid, 2-methylacetoacetic acid, tiglylglycine, and butanone. [provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:93](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:93) · Entrez [38](https://www.ncbi.nlm.nih.gov/gene/38) · UniProt [P24752](https://www.uniprot.org/uniprotkb/P24752) · Ensembl [ENSG00000075239](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075239)

## Data

Gene col 1108: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1108); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1108, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1108]; `tensor/DDL_lfc|DDL_z.npy` [1108]; `embed/gene_vectors.npy` [1108]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1108 or target_col == 1108). Every well: [[ACAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
