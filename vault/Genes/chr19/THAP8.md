---
symbol: "THAP8"
type: "gene"
col: 8428
ensembl_id: "ENSG00000161277"
name: "THAP domain containing 8"
location: "19q13.12"
module: 79
arm: "+"
pooled_cpm: 3.87
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# THAP8

*THAP domain containing 8* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.75× (z +6.4, q 1e-07, up in 18 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.405× (z -10.7, q 1e-23, down in 24 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.459× (z -9.2, q 1e-17, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF292]] (+0.67, fdr 1e-05), [[ZNF14]] (+0.64, fdr 1e-05), [[MXI1]] (+0.63, fdr 1e-05); moves opposite to [[HNRNPAB]] (-0.66, fdr 1e-05), [[GATAD2A]] (-0.65, fdr 7e-06), [[DOCK1]] (-0.62, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.75×** | +6.4 | 1e-07 | 18/40 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +5.7 | 4e-06 | 11/45 (PANC-1, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 0.003 | 6/45 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.006 | 6/44 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.007 | 11/45 (Hs 766T, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.009 | 4/47 (MIA PaCa-2, CHP-212, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.015 | 7/45 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.017 | 4/45 (LoVo, NCI-H2030, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.021 | 5/47 (SW480, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~8% here); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.034 | 4/24 (HOP62, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.041 | 7/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.071 | 11/43 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | 1.28× | +3.0 | 0.11 | 2/45 (SW 900, HEC-1-A) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8428.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.405×** | -10.7 | 1e-23 | 24/35 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -9.2 | 1e-17 | 26/46 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.471×** | -8.9 | 1e-16 | 29/46 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.567×** | -6.7 | 3e-09 | 21/44 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.642×** | -5.2 | 2e-05 | 13/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -4.7 | 3e-04 | 13/45 (Hs 766T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.686×** | -4.4 | 7e-04 | 13/41 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.701×** | -4.2 | 0.002 | 11/38 (C32, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.733×** | -3.7 | 0.016 | 12/45 (NCI-H1792, LS 180, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.726×** | -3.6 | 0.016 | 14/44 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.735×** | -3.5 | 0.026 | 13/28 (HS-578T, Hs 766T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.749×** | -3.4 | 0.032 | 9/38 (LOX-IMVI, KATO III, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.759×** | -3.2 | 0.051 | 12/43 (J82, CFPAC-1, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.609×** | -3.1 | 0.092 | 7/30 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.92 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.187× (z -11.2) |
| [[HS-578T (line)]] | alt | 5.64 | 0 | 2 (1 ⚠) | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0859× (z -9.5) |
| [[A-172 (line)]] | wt | 4.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 7.98 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0540× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 4.57 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0969× (z -9.0) |
| [[LS 180 (line)]] | wt | 5.08 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 1.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0576× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 4.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 5.49 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.72 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF292]] | +0.67 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.64 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[MXI1]] | +0.63 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[CLIP3]] | +0.63 | +0.69 / +0.49 | both halves | 1e-05 | STRING 407; ⚠ same locus (1.6 kb, same strand: neighbours can correlate without regulation) |
| [[RRAGD]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[EXOC1]] | +0.62 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PEX3]] | +0.61 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[SNX2]] | +0.61 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[PLEKHA2]] | +0.60 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[USP30]] | +0.60 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SNAPC3]] | +0.60 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[VPS37D]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPAB]] | -0.66 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.65 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[DOCK1]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[GNL3L]] | -0.61 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[UGGT2]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MTAP]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.59 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[TTL]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SLFNL1-AS1]] | -0.57 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SLC4A7]] | -0.57 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[SRPK1]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[SUSD1]] | -0.57 | -0.53 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers THAP8's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[PLEKHA6]] | B | PLEKHA6 activity lowers THAP8's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.35× higher at baseline in the lines without PLEKHA6 | 0.032 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity lowers THAP8's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[CLIP3]] | C | CLIP3 activity raises THAP8's level | lines that do not express CLIP3 (4) vs lines expressing it (46) | 2.09× lower at baseline in the lines without CLIP3 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: RAPGEF4, MEGF11, TMEM170B; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (6.4, -24.1); signed map (-25.1, -7.8). **Vector** length 48.3, 5.71% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.7 |
|  | [[Trametinib (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.4 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.9 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.7 | +2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.4 | -6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.0 | -0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | THAP domain containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,034,984-36,054,739 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32891 |
| Gene groups (HGNC) | THAP domain family |
| Matched by | ensembl_id |

UniProt [Q8NA92](https://www.uniprot.org/uniprotkb/Q8NA92) carries no function annotation.

**Summary**, from NCBI Gene [199745](https://www.ncbi.nlm.nih.gov/gene/199745):

> Predicted to enable DNA binding activity and zinc ion binding activity. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23191](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23191) · Entrez [199745](https://www.ncbi.nlm.nih.gov/gene/199745) · UniProt [Q8NA92](https://www.uniprot.org/uniprotkb/Q8NA92) · Ensembl [ENSG00000161277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161277)

## Data

Gene col 8428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8428); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8428]; `tensor/DDL_lfc|DDL_z.npy` [8428]; `embed/gene_vectors.npy` [8428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8428 or target_col == 8428). Every well: [[THAP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THAP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
