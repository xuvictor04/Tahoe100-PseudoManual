---
symbol: "CFL1P1-1"
type: "gene"
col: 16505
ensembl_id: "ENSG00000290782"
name: ""
location: ""
module: 21
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 44
n_dd_up: 19
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CFL1P1-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.77× (z +17.7, q 0e+00, up in 14 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +12.3, q 3e-32, up in 23 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.535× (z -5.4, q 3e-05, down in 17 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARMH1]] (+0.65, fdr 7e-06), [[ENO4]] (+0.64, fdr 7e-06), [[BTG1-DT]] (+0.64, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.77×** | +17.7 | 0e+00 | 14/15 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.34×** | +15.3 | 0e+00 | 5/5 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +12.3 | 3e-32 | 23/25 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.45×** | +11.9 | 1e-30 | 7/7 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +5.7 | 1e-06 | 15/40 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.83×** | +5.2 | 2e-05 | 13/40 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.67×** | +4.5 | 7e-04 | 8/39 (C-33 A, HEC-1-A, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.3 | 1e-03 | 7/39 (SW480, SHP-77, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.002 | 13/39 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.65×** | +4.0 | 0.004 | 2/23 (LS 180, A-427) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.007 | 9/33 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.55×** | +3.5 | 0.022 | 4/22 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.4 | 0.025 | 4/26 (BT-474, CFPAC-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.029 | 10/35 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.052 | 10/38 (PANC-1, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.080 | 7/39 (A498, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.082 | 9/36 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.087 | 3/24 (NCI-H23, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.535×** | -5.4 | 3e-05 | 17/36 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.541×** | -5.3 | 3e-05 | 18/40 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -3.7 | 0.034 | 14/37 (C-33 A, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.665×** | -3.5 | 0.062 | 10/33 (NCI-H2030, HOP62, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Fumaric acid (drug)]] 5 µM |  | 0.686× | -3.1 | 0.20 | 4/39 (Hs 766T, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.700× | -3.1 | 0.20 | 8/39 (NCI-H460, SNU-423, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 4.15 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.15× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 15.5 | 0 | 2 (1 ⚠) | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.199× (z -9.8) |
| [[PANC-1 (line)]] | alt | 5.52 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -9.1) |
| [[A498 (line)]] | wt | 2.70 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 21.6× (z +9.9) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 7.84 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0788× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 3.52 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.2× (z +9.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 1.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 38.6× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0709× (z -9.8) |
| [[A-172 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.396 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.415 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.366 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARMH1]] | +0.65 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[ENO4]] | +0.64 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[BTG1-DT]] | +0.64 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ETFBKMT]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CCDC3]] | +0.62 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[SNAP25-AS1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[DMXL1-DT]] | +0.61 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[GDPD4]] | +0.59 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[DNAJC27-AS1]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[RFPL1S]] | +0.58 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.58 | +0.51 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.537). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.2, 30.1); signed map (37.4, 4.9). **Vector** length 54.9, 8.70% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.8 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.6 | +17.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +12.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.1 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -2.0 |

## What is on record

> [!warning] No registry record
> CFL1P1-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16505); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16505]; `tensor/DDL_lfc|DDL_z.npy` [16505]; `embed/gene_vectors.npy` [16505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16505 or target_col == 16505). Every well: [[CFL1P1-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFL1P1-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
