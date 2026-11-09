---
symbol: "ZSCAN2"
type: "gene"
col: 10705
ensembl_id: "ENSG00000176371"
name: "zinc finger and SCAN domain containing 2"
location: "15q25.2"
module: 183
arm: "+"
pooled_cpm: 5.47
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# ZSCAN2

*zinc finger and SCAN domain containing 2* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 2.58× (z +12.1, q 6e-31, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.670× (z -5.1, q 2e-04, down in 13 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP30]] (+0.61, fdr 1e-05), [[FBXO44]] (+0.60, fdr 3e-05), [[SERAC1]] (+0.59, fdr 7e-06); moves opposite to [[C5AR1]] (-0.56, fdr 2e-05), [[SGMS2]] (-0.53, fdr 2e-05), [[PPIEL-1]] (-0.52, fdr 4e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSPAN33]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10705.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **2.58×** | +12.1 | 6e-31 | 39/45 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +11.3 | 2e-27 | 38/45 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +10.0 | 2e-21 | 29/41 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.19×** | +10.0 | 3e-21 | 30/46 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +8.4 | 3e-15 | 19/30 (HT-29, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.90×** | +8.2 | 3e-14 | 31/46 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.55×** | +5.6 | 2e-06 | 11/46 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +5.5 | 3e-06 | 15/45 (PANC-1, A-172, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.25×** | +5.4 | 4e-06 | 12/44 (PANC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +5.1 | 2e-05 | 18/42 (H4, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +5.1 | 2e-05 | 18/45 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.7 | 1e-04 | 9/43 (A549, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 7e-04 | 13/44 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.26×** | +4.2 | 0.001 | 11/46 (LOX-IMVI, A498, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.002 | 6/46 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.005 | 7/44 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.007 | 13/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10705.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -5.1 | 2e-04 | 13/45 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.699×** | -4.6 | 0.001 | 11/46 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.817×** | -3.7 | 0.044 | 16/40 (Panc 03.27, NCI-H1573, …) | rises with dose | composition shift |
| [[Isocorydine (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.091 | 4/45 (NCI-H460, RPMI-7951, …) | top dose only | position effect removed |
| [[Acetohexamide (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.091 | 12/45 (SW48, HepG2/C3A, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.769× | -3.2 | 0.11 | 9/45 (SW48, SW 1271, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10705. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.19 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0550× (z -13.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SHP-77 (line)]] | alt | 9.86 | 0 | 2 (1 ⚠) | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.102× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 5.64 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.116× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 8.80 | 0 | 1 | — | [[Auranofin (drug)]] 0.5 µM 0.0658× (z -9.3) |
| [[HT-29 (line)]] | alt | 6.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0681× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 4.39 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0679× (z -10.9) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H1792 (line)]] | alt | 8.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[Panc 03.27 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -8.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SW480 (line)]] | alt | 4.94 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change |
| [[A-172 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10705), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | +0.61 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.60 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[SERAC1]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[STPG1]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PRUNE1]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[NAPB]] | +0.57 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[ZFP14]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 | same gene group |
| [[TRAPPC2]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[DENND10]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[HSDL1]] | +0.55 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[BCL9]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[CGRRF1]] | +0.55 | +0.39 / +0.61 | both halves | 5e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5AR1]] | -0.56 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[SGMS2]] | -0.53 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[PPIEL-1]] | -0.52 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[INTS6]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[RB1]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[NSUN6]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZDHHC11]] | -0.51 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MYH15]] | -0.50 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[PPIEL]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PMFBP1]] | -0.50 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[TRIP12]] | -0.49 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[TEX14]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSPAN33]] | B | TSPAN33 activity raises ZSCAN2's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.59× lower at baseline in the lines without TSPAN33 | 0.017 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.6, -2.8); signed map (-31.8, -5.7). **Vector** length 55.5, 7.48% of its response variance represented; |z| ≥ 3 in 849 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +8.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.9 | +4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +10.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +5.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -2.4 | -2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | -2.0 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.8 |
|  | [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and SCAN domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:84,600,986-84,627,796 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20595, ZNF854; previously ZFP29 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7L9](https://www.uniprot.org/uniprotkb/Q7Z7L9) (Zinc finger and SCAN domain-containing protein 2):

> May be involved in transcriptional regulation during the post-meiotic stages of spermatogenesis.

**Summary**, from NCBI Gene [54993](https://www.ncbi.nlm.nih.gov/gene/54993):

> The protein encoded by this gene contains several copies of zinc finger motif, which is commonly found in transcriptional regulatory proteins. Studies in mice show that this gene is expressed during embryonic development, and specifically in the testis in adult mice, suggesting that it may play a role in regulating genes in germ cells. Alternative splicing of this gene results in several transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20994) · Entrez [54993](https://www.ncbi.nlm.nih.gov/gene/54993) · UniProt [Q7Z7L9](https://www.uniprot.org/uniprotkb/Q7Z7L9) · Ensembl [ENSG00000176371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176371)

## Data

Gene col 10705: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10705); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10705, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10705]; `tensor/DDL_lfc|DDL_z.npy` [10705]; `embed/gene_vectors.npy` [10705]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10705 or target_col == 10705). Every well: [[ZSCAN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZSCAN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
